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
