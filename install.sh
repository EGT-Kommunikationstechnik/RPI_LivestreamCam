#!/bin/bash
echo "Instaling LivestreamingCam"
apt-get install ffmpeg wget

mkdir ~/RPI_Livestreamcam
cd ~/RPI_Livestreamcam
wget "https://raw.githubusercontent.com/EGT-Kommunikationstechnik/RPI_LivestreamCam/main/automatik.py"
wget "https://raw.githubusercontent.com/EGT-Kommunikationstechnik/RPI_LivestreamCam/main/kill.sh"
wget "https://raw.githubusercontent.com/EGT-Kommunikationstechnik/RPI_LivestreamCam/main/stream.sh"
wget "https://raw.githubusercontent.com/EGT-Kommunikationstechnik/RPI_LivestreamCam/main/servo.py"
#echo "URL of the Command Server:"

##### Setingup CRON ########
#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "@reboot python ~/RPI_Livestreamcam/automation.py" >> mycron
echo "0    0    * * *  . ~/RPI_Livestreamcam/update.sh" >> mycron
#install new cron file
crontab mycron
rm mycron

echo "DONE"
