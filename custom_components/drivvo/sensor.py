import logging
from typing import Any
from datetime import datetime
import pytz

import voluptuous as vol

from homeassistant import config_entries, core
from homeassistant.components.sensor import (
    PLATFORM_SCHEMA,
    SensorEntity,
    SensorDeviceClass,
)
from homeassistant.const import STATE_UNKNOWN
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.issue_registry import IssueSeverity, async_create_issue
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from . import get_data_vehicle
from .const import (
    CONF_EMAIL,
    CONF_ID_VEHICLE,
    CONF_MODEL,
    CONF_PASSWORD,
    CONF_VEHICLES,
    DOMAIN,
    ICON,
    SCAN_INTERVAL,
)
from .sensors import SENSOR_TYPES, DrivvoSensorEntityDescription

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_EMAIL): cv.string,
        vol.Required(CONF_PASSWORD): cv.string,
        vol.Required(CONF_MODEL): cv.string,
        vol.Required(CONF_ID_VEHICLE): cv.string,
    }
)


async def async_setup_entry(
    hass: core.HomeAssistant,
    config_entry: config_entries.ConfigEntry,
    async_add_entities,
) -> None:
    """Setup sensor platform."""
    config = hass.data[DOMAIN][config_entry.entry_id]
    entities = []

    # Make sure we have a place to store coordinators
    hass.data.setdefault(f"{DOMAIN}_coordinators", {})

    for vehicle in config[CONF_VEHICLES]:
        # Create a unique update method for this specific vehicle
        async def _update_for_vehicle(vehicle_id=vehicle):
            return await get_data_vehicle(
                hass,
                user=config[CONF_EMAIL],
                password=config[CONF_PASSWORD],
                id_vehicle=vehicle_id,
            )

        # Get initial data for the vehicle
        vehicle_data = await get_data_vehicle(
            hass,
            user=config[CONF_EMAIL],
            password=config[CONF_PASSWORD],
            id_vehicle=vehicle,
        )

        if vehicle_data is not None:
            # Create coordinator for data updates
            coordinator = DataUpdateCoordinator(
                hass,
                _LOGGER,
                name=f"Drivvo {vehicle_data.identification}",
                update_interval=SCAN_INTERVAL,
                update_method=_update_for_vehicle,
            )

            # Store coordinator to prevent garbage collection
            hass.data[f"{DOMAIN}_coordinators"][vehicle] = coordinator

            # Fetch initial data
            await coordinator.async_config_entry_first_refresh()

            # Create sensor entities
            for description in SENSOR_TYPES:
                if description.key == "vehicle":
                    model = vehicle_data.model
                    entities.append(
                        DrivvoSensorEntity(
                            coordinator,
                            description,
                            vehicle_data.id,
                            vehicle_data.identification,
                            model,
                        )
                    )
                else:
                    entities.append(
                        DrivvoSensorEntity(
                            coordinator,
                            description,
                            vehicle_data.id,
                            vehicle_data.identification,
                        )
                    )
        else:
            async_create_issue(
                hass,
                DOMAIN,
                f"{vehicle}_vehicle_non_existent",
                is_fixable=False,
                severity=IssueSeverity.WARNING,
                translation_key="vehicle_non_existent",
                translation_placeholders={
                    "vehicle": vehicle,
                },
            )

    async_add_entities(entities)


async def async_setup_platform(
    hass: core.HomeAssistant,
    config: dict[str, Any],
    add_entities,
    discovery_info=False,
) -> bool:
    """Import to config flow."""
    _LOGGER.warning(
        "Configuration of Drivvo integration via YAML is deprecated."
        "Your configuration has been imported into the UI and can be"
        "removed from the configuration.yaml file."
    )

    async_create_issue(
        hass,
        DOMAIN,
        "yaml_deprecated",
        is_fixable=False,
        severity=IssueSeverity.WARNING,
        translation_key="yaml_deprecated",
    )

    hass.async_create_task(
        hass.config_entries.flow.async_init(
            DOMAIN,
            context={"source": config_entries.SOURCE_IMPORT},
            data=config,
        )
    )

    return True


class DrivvoSensorEntity(CoordinatorEntity, SensorEntity):
    """Representation of a Drivvo sensor."""

    entity_description: DrivvoSensorEntityDescription

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        description: DrivvoSensorEntityDescription,
        vehicle_id: str,
        vehicle_name: str,
        model: str = None,
    ) -> None:
        """Initialize the sensor entity."""
        super().__init__(coordinator)
        self.entity_description = description
        self._vehicle_id = vehicle_id
        self._vehicle_name = vehicle_name
        self._model = model

        # Set unique ID
        self._attr_unique_id = f"{vehicle_id}_{description.key}"

        # Set entity name
        self._attr_has_entity_name = True

        # Set device info
        self._attr_device_info = DeviceInfo(
            entry_type=dr.DeviceEntryType.SERVICE,  # Changed back from DEVICE to SERVICE
            identifiers={(DOMAIN, vehicle_id)},
            name=vehicle_name,
            manufacturer="Drivvo",
            model=f"{coordinator.data.manufacturer} {coordinator.data.model}",
            sw_version="2.0.0",
        )

    @property
    def native_value(self) -> Any:
        """Return the sensor value."""
        if self.coordinator.data is None:
            return STATE_UNKNOWN

        if self.entity_description.key == "vehicle" and self._model:
            return self._model

        try:
            if self.entity_description.value_fn:
                value = self.entity_description.value_fn(self.coordinator.data)

                # Convert string timestamps to datetime objects with timezone
                if (
                    self.entity_description.device_class == SensorDeviceClass.TIMESTAMP
                    and isinstance(value, str)
                ):
                    try:
                        # Parse the datetime string and make it timezone-aware
                        dt_obj = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
                        return dt_obj.replace(tzinfo=pytz.UTC)
                    except ValueError as e:
                        _LOGGER.error(f"Error parsing timestamp '{value}': {e}")
                        return STATE_UNKNOWN

                return value
        except (KeyError, AttributeError) as e:
            _LOGGER.error(f"Error getting value for {self.entity_description.key}: {e}")
            return STATE_UNKNOWN

        return STATE_UNKNOWN

    @property
    def icon(self) -> str:
        """Return the icon."""
        return self.entity_description.icon or ICON

    @property
    def native_unit_of_measurement(self) -> str | None:
        """Return the unit of measurement of this entity."""
        if (
            self.coordinator.data is not None
            and self.entity_description.unit_fn is not None
        ):
            return self.entity_description.unit_fn(self.coordinator.data)
        return self.entity_description.native_unit_of_measurement
