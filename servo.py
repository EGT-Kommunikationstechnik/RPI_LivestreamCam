import RPi.GPIO as GPIO
import time
import os
import time
import requests

PANservoPIN = 17
#TILTservoPIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(PANservoPIN, GPIO.OUT)
#GPIO.setup(TILTservoPIN, GPIO.OUT)

p = GPIO.PWM(PANservoPIN,  50) # GPIO 17 als PWM mit 50Hz
#t = GPIO.PWM(TILTservoPIN, 60) #27
pan = 7.0
datei = open('cam_nr.config','r')
cam_nr = int(datei.read())
i=0 #loop count
try:
  while 1:
    receive = requests.get('http://sat-master.uberrider.de/cam_ptz.php?ch='+str(cam_nr))
    print receive.text
    if receive.text == "OFF":
      p.stop()
      print "Servo Aus"
    else:
      if float(receive.text) == pan and  i<10:
        print( "Noch auf ", pan ,i)
        i = i + 1
      else:
        i = 0
        pan = float(receive.text)
        p.start(pan)
        p.ChangeDutyCycle(pan)
        time.sleep(1.0)
        p.stop()
        print("PAN:",receive.text)
        pan = float(receive.text)
    time.sleep(0.5)

except KeyboardInterrupt:
  GPIO.cleanup()





