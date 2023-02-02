# Nuki MQTT auto. Discovery

This repository is a fork of [MattDog06/Nuki-MQTT-auto.-Discovery](https://github.com/MattDog06/Nuki-MQTT-auto.-Discovery)

[![hass_badge](https://img.shields.io/badge/Platform-Home%20Assistant-blue.svg)](https://www.home-assistant.io)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)
[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Nardol&repository=Nuki-MQTT-auto.-Discovery&category=python_script)

Python script for creating Home Assistant MQTT auto. discovery topics for a Nuki Smart Lock 3.0 Pro with enabled MQTT client. (currently only available in the beta firmware) Execute this script once to create a MQTT device with all necessary entities.

## Usage

Just copy the URL of this repository and add it under HACS --> Custom Repositories (Category: Python-Script)

### Parameters

| Parameter | Type | Required | Description | Example |
| ---- | :--: | :------: | ----------- | ------- |
| device_id | string | Yes | The device ID also known as Nuki Smart Lock ID. | 12345ABC |
| device_name | string | Yes | The device name | Front Door Lock |
| device_model | string | Yes | The device model | Smart Lock 3.0 Pro |
| discovery_topic | string | No | The home assistant auto. discovery topic (Default: homeassistant) | homeassistant |
| door_sensor_available | boolean | No | If true, the door sensor data is also discovered (Default: false) | true |
| keypad_available | boolean | No | 	If true, the keypad data is also discovered (Default: false) | false |
| remove_lock | boolean | No | 	If true, all MQTT Nuki related topics are removed (Default: false) | false |

### Example

```yaml
service: python_script.nuki_mqtt_discovery
data:
  device_id: 12345ABC
  device_name: Front Door Lock
  device_model: Smart Lock 3.0 Pro
  discovery_topic: homeassistant
  door_sensor_available: true
  keypad_available: false
```

### Home Assistant Device
![Sample](homeassistant_device.png)

## Differences with original script
* The smartlock ID is used for entity unique IDs instead of the name which could be changed
Using this method, if the smartlock is renamed in the Nuki app, the existing entities will be updated instead of create new entities
* Node ID is not used anymore for MQTT topics
* MQTT abbreviations are used
* Locking, unlocking and jammed states are implemented. This change should be visible from Home Assistant 2023.2
* Open and opening states are removed, these don't exist in Home Assistant for lock entities
* Apply conventional namming for entities, for example the door sensor of the smartlock Front door will be named Front door Door sensor instead of Front door Door Sensor
* In the root of this repository, there is now a script to remove original device and entities.
It uses the same parameters you used to add the smartlock entities, `nuki_remove_old` has to be used instead of `nuki_mqtt_discovery` when calling the service, you must place the `nuki_remove_old.py` to the `python_script` subdirectory of your Home Assistant configuration directory
