import paho.mqtt.client as mqtt
import time
broker=""
port=
username=""
password=""
def on_connect(client, userdata, flags, rc):
        if rc==0:
                print("Connect"+str(rc))
                client.subscribe("Topicname")
        else:
                print("Bad connection code=", rc)
def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        p=str(msg.payload)
        pri(p)
def pri(power):
        print(power)
client=mqtt.Client("sub")
client.username_pw_set(username, password)
client.on_connect=on_connect
client.on_message=on_message
print("Connecting to broker", broker)
client.connect(broker,port)
time.sleep(1)
print("in main loop")
client.loop_forever()
client.disconnect()

