# notify
print('RUN: main.py')

# MQTT broker IP address
mqtt_server = '192.168.0.6'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'notification'
topic_pub = b'hello'



def sub_cb(topic, msg):
  print('rcv ',(topic, msg))

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_pub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_pub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(5)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    new_message = client.check_msg()
    if new_message != None:
      print('msg ',new_message)
    time.sleep(1)
  except OSError as e:
    restart_and_reconnect()