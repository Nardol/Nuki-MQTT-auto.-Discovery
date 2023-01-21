# Parameters
DEVICE_ID = "device_id"
DEVICE_NAME = "device_name"
DEVICE_MODEL = "device_model"
DISCOVERY_TOPIC = "discovery_topic"
DOOR_SENSOR_AVAILABLE = "door_sensor_available"
KEYPAD_AVAILABLE = "keypad_available"

DEFAULT_DISCOVERY_TOPIC = "homeassistant"


def get_error_message(parameter, value):
  return "Parameter '" + parameter + "' is required! Current value is '" + str(value) + "'."


def get_object_id(name):  
  return name.replace(" ", "_").replace("-", "_").lower()


def to_json(dictonary):
  return '{}'.format(dictonary).replace("\'", "\"").replace("\"\"", "\'")


def get_discovery_topic(discovery_topic, component, node_id, name):
  return discovery_topic + "/" + component + "/" + node_id + "/" + get_object_id(name) + "/config"


def publish(hass, topic, payload):
  data = {
    "topic": topic,
    "payload": payload,
    "retain": 'true'
  }

  hass.services.call("mqtt", "publish", data)


def main(hass, data):
  device_id = data.get(DEVICE_ID)
  device_name = data.get(DEVICE_NAME)
  discovery_topic = data.get(DISCOVERY_TOPIC) or DEFAULT_DISCOVERY_TOPIC
  door_sensor_available = data.get(DOOR_SENSOR_AVAILABLE) or False
  keypad_available = data.get(KEYPAD_AVAILABLE) or False

  if isinstance(device_id, int): # Because of hex device id, always convert it to string
    device_id = str(device_id)

  if device_id == None or device_id == "":
    logger.error(get_error_message(DEVICE_ID, device_id))
    return
  
  if device_name == None or device_name == "":
    logger.error(get_error_message(DEVICE_NAME, device_name))
    return


  # Lock
  name = device_name
  publish(hass, get_discovery_topic(discovery_topic, "lock", device_id, name),"")

  # Battery critical
  name = device_name + " Battery Critical"
  publish(hass, get_discovery_topic(discovery_topic, "binary_sensor", device_id, name), "")

  # Battery charge state
  name = device_name + " Battery"
  publish(hass, get_discovery_topic(discovery_topic, "sensor", device_id, name), "")

  # Battery charging
  name = device_name + " Battery Charging"
  publish(hass, get_discovery_topic(discovery_topic, "binary_sensor", device_id, name), "")

  if door_sensor_available:
    # Door sensor
    name = device_name + " Door Sensor"
    publish(hass, get_discovery_topic(discovery_topic, "binary_sensor", device_id, name), "")

    # Door sensor battery critical
    name = device_name + " Door Sensor Battery Critical"
    publish(hass, get_discovery_topic(discovery_topic, "binary_sensor", device_id, name), "")

  if keypad_available:
    # Keypad battery critical
    name = device_name + " Keypad Battery Critical"
    publish(hass, get_discovery_topic(discovery_topic, "binary_sensor", device_id, name), "")

  # Unlatch button
  name = device_name + " Unlatch"
  publish(hass, get_discovery_topic(discovery_topic, "button", device_id, name), "")

  # Lock'n'Go button
  name = device_name + " Lock-n-Go"
  publish(hass, get_discovery_topic(discovery_topic, "button", device_id, name), "")

  # Lock'n'Go with unlatch button
  name = device_name + " Lock-n-Go With Unlatch"
  publish(hass, get_discovery_topic(discovery_topic, "button", device_id, name), "")


#main(hass, data)
