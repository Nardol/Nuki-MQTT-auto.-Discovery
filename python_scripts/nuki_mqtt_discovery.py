# Parameters
DEVICE_ID = "device_id"
DEVICE_NAME = "device_name"
DEVICE_MODEL = "device_model"
DISCOVERY_TOPIC = "discovery_topic"
DOOR_SENSOR_AVAILABLE = "door_sensor_available"
KEYPAD_AVAILABLE = "keypad_available"
REMOVE_LOCK = "remove_lock"

DEFAULT_DISCOVERY_TOPIC = "homeassistant"

# Topics
TOPIC_BASE = "nuki"
TOPIC_STATE = "state"
TOPIC_LOCK_ACTION = "lockAction"
TOPIC_CONNECTED = "connected"
TOPIC_BATTERY_CRITICAL = "batteryCritical"
TOPIC_BATTERY_CHARGE_STATE = "batteryChargeState"
TOPIC_BATTERY_CHARGING = "batteryCharging"
TOPIC_DOOR_SENSOR_STATE = "doorsensorState"
TOPIC_DOOR_SENSOR_BATTERY_CRITICAL = "doorsensorBatteryCritical"
TOPIC_KEYPAD_BATTERY_CRITICAL = "keypadBatteryCritical"

# Lock states
STATE_UNCALIBRATED = 0
STATE_LOCKED = 1
STATE_UNLOCKING = 2
STATE_UNLOCKED = 3
STATE_LOCKING = 4
STATE_UNLATCHED = 5
STATE_UNLOCKED_LOCKNGO = 6
STATE_UNLATCHING = 7
STATE_MOTOR_BLOCKED = 254
STATE_UNDEFINED = 255

# Lock actions
ACTION_UNLOCK = 1
ACTION_LOCK = 2
ACTION_UNLATCH = 3
ACTION_LOCKNGO = 4
ACTION_LOCKNGO_UNLATCH = 5
ACTION_FULL_LOCK = 6
ACTION_FOB = 80
ACTION_BUTTON = 90

# Door sensor states
DOOR_STATE_DEACTIVATED = 1
DOOR_STATE_DOOR_CLOSED = 2
DOOR_STATE_DOOR_OPENED = 3
DOOR_STATE_DOOR_STATE_UNKNOWN = 4
DOOR_STATE_CALIBRATING = 5
DOOR_STATE_UNCALIBRATED = 16
DOOR_STATE_TAMPERED = 240
DOOR_STATE_UNKNOWN = 255


def get_error_message(parameter, value):
  return "Parameter '" + parameter + "' is required! Current value is '" + str(value) + "'."


def to_json(dictionary):
  return '{}'.format(dictionary).replace("\'", "\"").replace("\"\"", "\'")


def get_discovery_topic(discovery_topic, component, node_id, name):
  return discovery_topic + "/" + component + "/nuki_" + node_id + "_" + name + "/config"


def get_base_topic(device_id):
  return TOPIC_BASE + "/" + device_id


def get_topic(topic):
  return "~/"+topic


def get_device(device_id, device_name, device_model):
  return {
    'ids': [
        "nuki_"+device_id
    ],
    'mf': 'Nuki',
    'name': device_name,
    'mdl': device_model
  }


def get_lock_payload(device_id, device_name, device_model, name):
  return to_json({
    '~': get_base_topic(device_id),
    'avty_t': get_topic(TOPIC_CONNECTED),
    'pl_avail': 'true',
    'pl_not_avail': 'false',
    'dev': get_device(device_id, device_name, device_model),
    'name': name,
    'uniq_id': "nuki_"+device_id+"_lock",
    'cmd_t': get_topic(TOPIC_LOCK_ACTION),
    'pl_lock': str(ACTION_LOCK),
    'pl_unlk': str(ACTION_UNLOCK),
    'pl_open': str(ACTION_UNLATCH),
    'stat_t': get_topic(TOPIC_STATE),
    'stat_locked': str(STATE_LOCKED),
    'stat_locking': str(STATE_LOCKING),
    'stat_unlocked': str(STATE_UNLOCKED),
    'stat_unlocking': str(STATE_UNLOCKING),
    'stat_jam': str(STATE_MOTOR_BLOCKED),
    'val_tpl': '{% if value == \'\'' + str(STATE_UNLOCKED_LOCKNGO) + '\'\'%}' + str(STATE_UNLOCKED) + '{% else %}{{value}}{% endif %}'
  })


def get_battery_critical_payload(device_id, device_name, device_model, name):
  return to_json({
    '~': get_base_topic(device_id),
    'avty_t': get_topic(TOPIC_CONNECTED),
    'pl_avail': 'true',
    'pl_not_avail': 'false',
    'dev': get_device(device_id, device_name, device_model),
    'name': name,
    'uniq_id': "nuki_"+device_id+"_lock_battery_critical",
    'dev_cla': 'battery',
    'ent_cat': 'diagnostic',
    'stat_t': get_topic(TOPIC_BATTERY_CRITICAL),
    'pl_off': 'false',
    'pl_on': 'true'
  })


def get_battery_charge_state_payload(device_id, device_name, device_model, name):
  return to_json({
    '~': get_base_topic(device_id),
    'avty_t': get_topic(TOPIC_CONNECTED),
    'pl_avail': 'true',
    'pl_not_avail': 'false',
    'dev': get_device(device_id, device_name, device_model),
    'name': name,
    'uniq_id': "nuki_"+device_id+"_lock_battery_percent",
    'dev_cla': 'battery',
    'ent_cat': 'diagnostic',
    'stat_t': get_topic(TOPIC_BATTERY_CHARGE_STATE),
    'stat_cla': 'measurement',
    'unit_of_meas': '%'
  })


def get_battery_charging_payload(device_id, device_name, device_model, name):
  return to_json({
    '~': get_base_topic(device_id),
    'avty_t': get_topic(TOPIC_CONNECTED),
    'pl_avail': 'true',
    'pl_not_avail': 'false',
    'dev': get_device(device_id, device_name, device_model),
    'name': name,
    'uniq_id': "nuki_"+device_id+"_battery_charging",
    'dev_cla': 'battery_charging',
    'ent_cat': 'diagnostic',
    'stat_t': get_topic(TOPIC_BATTERY_CHARGING),
    'pl_off': 'false',
    'pl_on': 'true'
  })


def get_door_sensor_payload(device_id, device_name, device_model, name):
  return to_json({
    '~': get_base_topic(device_id),
    'avty_t': get_topic(TOPIC_CONNECTED),
    'pl_avail': 'true',
    'pl_not_avail': 'false',
    'dev': get_device(device_id, device_name, device_model),
    'name': name,
    'uniq_id': "nuki_"+device_id+"_door_sensor",
    'dev_cla': 'door',
    'pl_off': str(DOOR_STATE_DOOR_CLOSED),
    'pl_on': str(DOOR_STATE_DOOR_OPENED),
    'stat_t': get_topic(TOPIC_DOOR_SENSOR_STATE),
  })


def get_door_sensor_battery_critical_payload(device_id, device_name, device_model, name):
  return to_json({
    '~': get_base_topic(device_id),
    'avty_t': get_topic(TOPIC_CONNECTED),
    'pl_avail': 'true',
    'pl_not_avail': 'false',
    'dev': get_device(device_id, device_name, device_model),
    'name': name,
    'uniq_id': "nuki_"+device_id+"_door_sensor_battery_critical",
    'dev_cla': 'battery',
    'ent_cat': 'diagnostic',
    'stat_t': get_topic(TOPIC_DOOR_SENSOR_BATTERY_CRITICAL),
    'pl_off': 'false',
    'pl_on': 'true'
  })


def get_keypad_battery_critical_payload(device_id, device_name, device_model, name):
  return to_json({
    '~': get_base_topic(device_id),
    'avty_t': get_topic(TOPIC_CONNECTED),
    'pl_avail': 'true',
    'pl_not_avail': 'false',
    'dev': get_device(device_id, device_name, device_model),
    'name': name,
    'uniq_id': "nuki_"+device_id+"_keypad_battery_critical",
    'dev_cla': 'battery',
    'ent_cat': 'diagnostic',
    'stat_t': get_topic(TOPIC_KEYPAD_BATTERY_CRITICAL),
    'pl_off': 'false',
    'pl_on': 'true'
  })


def get_button_payload(device_id, device_name, device_model, name, action, action_id):
  return to_json({
    '~': get_base_topic(device_id),
    'avty_t': get_topic(TOPIC_CONNECTED),
    'pl_avail': 'true',
    'pl_not_avail': 'false',
    'dev': get_device(device_id, device_name, device_model),
    'name': name,
    'uniq_id': "nuki_"+device_id+"_"+action_id+"_button",
    'cmd_t': get_topic(TOPIC_LOCK_ACTION),
    'pl_prs': str(action)
  })


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
  device_model = data.get(DEVICE_MODEL)
  discovery_topic = data.get(DISCOVERY_TOPIC) or DEFAULT_DISCOVERY_TOPIC
  door_sensor_available = data.get(DOOR_SENSOR_AVAILABLE) or False
  keypad_available = data.get(KEYPAD_AVAILABLE) or False
  remove_lock = data.get(REMOVE_LOCK) or False

  if isinstance(device_id, int): # Because of hex device id, always convert it to string
    device_id = str(device_id)

  if device_id == None or device_id == "":
    logger.error(get_error_message(DEVICE_ID, device_id))
    return
  
  if device_name == None or device_name == "":
    logger.error(get_error_message(DEVICE_NAME, device_name))
    return

  if device_model == None or device_model == "":
    logger.error(get_error_message(DEVICE_MODEL, device_model))
    return

  if remove_lock:
    logger.warning("Uninstalling")

  # Lock
  name = device_name
  publish(hass, get_discovery_topic(discovery_topic, "lock", device_id, "lock"),
    get_lock_payload(device_id, device_name, device_model, name) if not remove_lock else "")

  # Battery critical
  name = device_name + " Battery critical"
  publish(hass, get_discovery_topic(discovery_topic, "binary_sensor", device_id, "lock_battery_critical"), 
    get_battery_critical_payload(device_id, device_name, device_model, name) if not remove_lock else "")

  # Battery charge state
  name = device_name + " Battery"
  publish(hass, get_discovery_topic(discovery_topic, "sensor", device_id, "battery_percent"),
    get_battery_charge_state_payload(device_id, device_name, device_model, name) if not remove_lock else "")

  # Battery charging
  name = device_name + " Battery charging"
  publish(hass, get_discovery_topic(discovery_topic, "binary_sensor", device_id, "battery_charging"),
    get_battery_charging_payload(device_id, device_name, device_model, name) if not remove_lock else "")

  if door_sensor_available:
    # Door sensor
    name = device_name + " Door sensor"
    publish(hass, get_discovery_topic(discovery_topic, "binary_sensor", device_id, "door_sensor"),
      get_door_sensor_payload(device_id, device_name, device_model, name) if not remove_lock else "")

    # Door sensor battery critical
    name = device_name + " Door sensor battery critical"
    publish(hass, get_discovery_topic(discovery_topic, "binary_sensor", device_id, "door_sensor_battery_critical"), 
      get_door_sensor_battery_critical_payload(device_id, device_name, device_model, name) if not remove_lock else "")

  if keypad_available:
    # Keypad battery critical
    name = device_name + " Keypad battery critical"
    publish(hass, get_discovery_topic(discovery_topic, "binary_sensor", device_id, "keypad_battery_critical"), 
      get_keypad_battery_critical_payload(device_id, device_name, device_model, name) if not remove_lock else "")

  # Unlatch button
  name = device_name + " Unlatch"
  publish(hass, get_discovery_topic(discovery_topic, "button", device_id, "unlatch_button"),
    get_button_payload(device_id, device_name, device_model, name, ACTION_UNLATCH, "unlatch") if not remove_lock else "")

  # Lock'n'Go button
  name = device_name + " Lock-n-Go"
  publish(hass, get_discovery_topic(discovery_topic, "button", device_id, "lockngo_button"),
    get_button_payload(device_id, device_name, device_model, name, ACTION_LOCKNGO, "lock_n_go") if not remove_lock else "")

  # Lock'n'Go with unlatch button
  name = device_name + " Lock-n-Go with unlatch"
  publish(hass, get_discovery_topic(discovery_topic, "button", device_id, "lock_n_go_unlatch"),
    get_button_payload(device_id, device_name, device_model, name, ACTION_LOCKNGO_UNLATCH, "lock_n_go_unlatch") if not remove_lock else "")


main(hass, data)
