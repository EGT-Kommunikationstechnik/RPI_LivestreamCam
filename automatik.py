import os
import time

datei = open('cam_nr.config','r')
cam_nr = int(datei.read())
time.sleep(60) #Warten bis alles da ist
taget=""
while 1:
	import requests
	receive = requests.get('http://sat-master.uberrider.de/cam.php?ch='+str(cam_nr))
	cmd=""
	print receive.text
	if receive.text == "OFF":
		cmd=". /home/pi/kill.sh"
                print cmd
                stream = os.system(cmd)
		taget=""
	else:
		cmd=". /home/pi/stream.sh  " + receive.text + " &"
		if receive.text != taget:
			taget=receive.text
			print cmd
			stream = os.system(cmd)
		else:
			print "Noch immer " + taget
	time.sleep(10)
