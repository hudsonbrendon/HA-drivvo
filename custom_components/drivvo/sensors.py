"""Sensor platform for Drivvo integration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

from homeassistant.components.sensor import (
    SensorEntityDescription,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.const import (
    UnitOfLength,
    UnitOfVolume,
)

from .units import UnitOfFuelEfficiency


@dataclass
class DrivvoSensorEntityDescription(SensorEntityDescription):
    """Class describing Drivvo sensor entities."""

    value_fn: Optional[Callable] = None


SENSOR_TYPES: tuple[DrivvoSensorEntityDescription, ...] = (
    DrivvoSensorEntityDescription(
        key="refuelling_total",
        translation_key="refuelling_total",
        name="Refuelling Total",
        icon="mdi:counter",
        state_class=SensorStateClass.TOTAL,
        value_fn=lambda data: data.refuelling_total,
    ),
    DrivvoSensorEntityDescription(
        key="vehicle",
        translation_key="vehicle",
        name="Vehicle",
        icon="mdi:car",
        value_fn=lambda data, model: model,
    ),
    DrivvoSensorEntityDescription(
        key="odometer",
        translation_key="odometer_value",
        name="Odometer",
        icon="mdi:speedometer",
        device_class=SensorDeviceClass.DISTANCE,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement=UnitOfLength.KILOMETERS,
        value_fn=lambda data: data.odometer,
    ),
    DrivvoSensorEntityDescription(
        key="odometer_date",
        translation_key="odometer_date",
        name="Odometer Date",
        icon="mdi:calendar",
        device_class=SensorDeviceClass.TIMESTAMP,
        value_fn=lambda data: data.odometer_date,
    ),
    DrivvoSensorEntityDescription(
        key="refuelling_last_average",
        translation_key="refuelling_last_average",
        name="Refuelling Last Average",
        icon="mdi:fuel",
        device_class=SensorDeviceClass.VOLUME_FLOW_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement=UnitOfFuelEfficiency.KILOMETERS_PER_LITER,
        value_fn=lambda data: data.refuelling_last_average,
        suggested_display_precision=2,
    ),
    DrivvoSensorEntityDescription(
        key="refuelling_general_average",
        translation_key="refuelling_general_average",
        name="Refuelling General Average",
        icon="mdi:fuel",
        device_class=SensorDeviceClass.VOLUME_FLOW_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement=UnitOfFuelEfficiency.KILOMETERS_PER_LITER,
        value_fn=lambda data: data.refuelling_general_average,
        suggested_display_precision=2,
    ),
    DrivvoSensorEntityDescription(
        key="refuelling_station",
        translation_key="refuelling_station",
        name="Refuelling Station",
        icon="mdi:gas-station",
        value_fn=lambda data: data.refuelling_station,
    ),
    DrivvoSensorEntityDescription(
        key="refuelling_type",
        translation_key="refuelling_type",
        name="Refuelling Type",
        icon="mdi:gas-station",
        value_fn=lambda data: data.refuelling_type,
    ),
    DrivvoSensorEntityDescription(
        key="refuelling_reason",
        translation_key="refuelling_reason",
        name="Refuelling Reason",
        icon="mdi:information-outline",
        value_fn=lambda data: data.refuelling_reason,
    ),
    DrivvoSensorEntityDescription(
        key="refuelling_date",
        translation_key="refuelling_date",
        name="Refuelling Date",
        icon="mdi:calendar",
        device_class=SensorDeviceClass.TIMESTAMP,
        value_fn=lambda data: data.refuelling_date,
    ),
    DrivvoSensorEntityDescription(
        key="refuelling_value",
        translation_key="refuelling_value",
        name="Refuelling Value",
        icon="mdi:cash",
        device_class=SensorDeviceClass.MONETARY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement=data.currency,
        value_fn=lambda data: data.refuelling_value,
        suggested_display_precision=2,
    ),
    DrivvoSensorEntityDescription(
        key="refuelling_price",
        translation_key="refuelling_price",
        name="Refuelling Price",
        icon="mdi:cash",
        device_class=SensorDeviceClass.MONETARY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement=data.currency,
        value_fn=lambda data: data.refuelling_price,
        suggested_display_precision=2,
    ),
    DrivvoSensorEntityDescription(
        key="refuelling_value_total",
        translation_key="refuelling_value_total",
        name="Refuelling Value Total",
        icon="mdi:cash",
        device_class=SensorDeviceClass.MONETARY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement=data.currency,
        value_fn=lambda data: data.refuelling_value_total,
        suggested_display_precision=2,
    ),
    DrivvoSensorEntityDescription(
        key="refuelling_tank_full",
        translation_key="refuelling_tank_full",
        name="Refuelling Tank Full",
        icon="mdi:gas-station",
        value_fn=lambda data: data.refuelling_tank_full,
    ),
    DrivvoSensorEntityDescription(
        key="refuelling_distance",
        translation_key="refuelling_distance",
        name="Refuelling Distance",
        icon="mdi:road",
        device_class=SensorDeviceClass.DISTANCE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement=UnitOfLength.KILOMETERS,
        value_fn=lambda data: data.refuelling_distance,
    ),
    DrivvoSensorEntityDescription(
        key="refuelling_price_lowest",
        translation_key="refuelling_price_lowest",
        name="Refuelling Price Lowest",
        icon="mdi:cash",
        device_class=SensorDeviceClass.MONETARY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement=data.currency,
        value_fn=lambda data: data.refuelling_price_lowest,
        suggested_display_precision=2,
    ),
    DrivvoSensorEntityDescription(
        key="refuelling_volume",
        translation_key="refuelling_volume",
        name="Refuelling Volume",
        icon="mdi:fuel",
        device_class=SensorDeviceClass.VOLUME,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement=UnitOfVolume.LITERS,
        value_fn=lambda data: data.refuelling_volume,
        suggested_display_precision=2,
    ),
    DrivvoSensorEntityDescription(
        key="refuelling_volume_total",
        translation_key="refuelling_volume_total",
        name="Refuelling Volume Total",
        icon="mdi:fuel",
        device_class=SensorDeviceClass.VOLUME,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement=UnitOfVolume.LITERS,
        value_fn=lambda data: data.refuelling_volume_total,
        suggested_display_precision=2,
    ),
)
