import paho.mqtt.client as mqtt
from time import sleep

# define static variable
# broker = "localhost" # for local connection
broker = "broker.hivemq.com"  # for online version
port = 1883
timeout = 60

username = 'campuspedia'
password = 'qlue'
topic = "Campuspedia/lampu/status"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
def on_publish(client,userdata,result):
	print("data published \n")
	


client1 = mqtt.Client("device1")
client1.username_pw_set(username=username,password=password)
client1.on_connect = on_connect
client1.on_publish = on_publish
client1.connect(broker,port,timeout)


count = 0
while count < 5:
	status = str(input("Do you want the lamp turn On or Off? "))
	message = status
	ret = client1.publish(topic,payload=message)
	sleep(1)
	count = count + 1




