![hacs_badge](https://img.shields.io/badge/hacs-custom-orange.svg)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://github.com/hacs/integration)
[![hassfest](https://github.com/hudsonbrendon/HA-drivvo/actions/workflows/hassfest.yaml/badge.svg)](https://github.com/hudsonbrendon/HA-drivvo/actions/workflows/hassfest.yaml)
[![HACS Action](https://github.com/hudsonbrendon/HA-drivvo/actions/workflows/hacs.yaml/badge.svg)](https://github.com/hudsonbrendon/HA-drivvo/actions/workflows/hacs.yaml)
[![Dependabot Updates](https://github.com/hudsonbrendon/HA-drivvo/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/hudsonbrendon/HA-drivvo/actions/workflows/dependabot-updates)

# Drivvo Custom Integration Home Assistant

![topo.png](topo.png)

Custom integration for the Home Assistant to obtain information present in [drivvo.com](https://www.drivvo.com/).

## Install

### Installation via HACS

Have HACS installed, this will allow you to update easily.

Adding Drivvo to HACS can be using this button:

[![image](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=hudsonbrendon&repository=HA-drivvo&category=integration)

If the button above doesn't work, add `https://github.com/hudsonbrendon/HA-drivvo` as a custom repository of type Integration in HACS.

- Click Install on the `Drivvo` integration.
- Restart the Home Assistant.

### Manual installation

- Copy `drivvo`  folder from [latest release](https://github.com/hudsonbrendon/HA-drivvo/releases/latest) to your `<config dir>/custom_components/` directory.
- Restart the Home Assistant.

## Configuration

Adding Drivvo to your Home Assistant instance can be done via the UI using this button:

[![image](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start?domain=drivvo)

### Manual Configuration

If the button above doesn't work, you can also perform the following steps manually:

* Navigate to your Home Assistant instance.
* In the sidebar, click Settings.
* From the Setup menu, select: Devices & Services.
* In the lower right corner, click the Add integration button.
* In the list, search and select `Drivvo`.
* Follow the on-screen instructions to complete the setup.

## Available Sensors

After the integration is set up, the following sensors will be available for each configured vehicle:

- **Vehicle**: Vehicle name and model
- **Odometer**: Current vehicle odometer reading
- **Odometer Date**: Date of last odometer update
- **Refuelling Total**: Number of total refuelling events
- **Refuelling Last Average**: Last fuel consumption average
- **Refuelling General Average**: General fuel consumption average
- **Refuelling Station**: Last refuelling station used
- **Refuelling Type**: Type of fuel used
- **Refuelling Reason**: Reason for the last refuelling
- **Refuelling Date**: Date of last refuelling
- **Refuelling Value**: Cost of last refuelling
- **Refuelling Price**: Price per liter/gallon of last refuelling
- **Refuelling Value Total**: Total cost of all refuellings
- **Refuelling Tank Full**: Whether the tank was filled completely
- **Refuelling Distance**: Distance traveled since last refuelling
- **Refuelling Price Lowest**: Lowest fuel price recorded
- **Refuelling Volume**: Volume of fuel in last refuelling
- **Refuelling Volume Total**: Total volume of fuel refuelled

## Debugging

To enable debug for Drivvo integration, add following to your `configuration.yaml`:
```yaml
logger:
  default: info
  logs:
    custom_components.drivvo: debug
```

## Making a Dashboard Card

Here's an example of a dashboard card using the new sensors. Replace the entity IDs with your own vehicle entities:

```yaml
type: vertical-stack
cards:
  - type: entities
    title: Vehicle Information
    entities:
      - entity: sensor.my_vehicle
      - entity: sensor.odometer
      - entity: sensor.odometer_date
      - entity: sensor.refuelling_total

  - type: horizontal-stack
    cards:
      - type: gauge
        name: Fuel Efficiency
        entity: sensor.refuelling_general_average
        min: 0
        max: 20
        severity:
          green: 12
          yellow: 8
          red: 0

      - type: gauge
        name: Last Refuelling
        entity: sensor.refuelling_volume
        min: 0
        max: 60
        unit: L
        severity:
          green: 0
          yellow: 30
          red: 50

  - type: history-graph
    title: Fuel Price History
    entities:
      - entity: sensor.refuelling_price
      - entity: sensor.refuelling_price_lowest
    hours_to_show: 168
    refresh_interval: 0

  - type: statistics-graph
    title: Refuelling Costs
    entities:
      - entity: sensor.refuelling_value
    period: month
    stat_types:
      - mean
      - sum
```

A more complex example with multiple visualizations:

```yaml
type: custom:apexcharts-card
chart_type: line
header:
  title: Vehicle Statistics
  show: true
  show_states: true
  colorize_states: true
series:
  - entity: sensor.odometer
    name: Odometer
    unit: km
  - entity: sensor.refuelling_price
    name: Fuel Price
    unit: €
    float_precision: 2
  - entity: sensor.refuelling_value
    name: Refuelling Cost
    unit: €
    float_precision: 2
  - entity: sensor.refuelling_value_total
    name: Total Cost
    unit: €
    float_precision: 2
  - entity: sensor.refuelling_distance
    name: Distance Between Refuellings
    unit: km
  - entity: sensor.refuelling_general_average
    name: Fuel Efficiency
    unit: km/L
    float_precision: 2
```

![logo.png](logo.png)

[buymecoffee]: https://www.buymeacoffee.com/hudsonbrendon
[buymecoffeebedge]: https://camo.githubusercontent.com/cd005dca0ef55d7725912ec03a936d3a7c8de5b5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6275792532306d6525323061253230636f666665652d646f6e6174652d79656c6c6f772e737667
