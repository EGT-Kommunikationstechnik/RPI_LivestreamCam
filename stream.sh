#!/bin/bash
killall ffmpeg
killall raspivid
raspivid -t 0 -w 1920 -h 1080 -fps 25 -l -n -b 3000000 -o - |\
ffmpeg -thread_queue_size 1024  -i - \
 -itsoffset 5.0 -f alsa  -i plughw:1,0  -ar 44100 \
 -c:v copy -c:a aac -strict experimental -b:v 2000k -f flv rtmp://sat1.uberrider.de/$1/uber \
  &>>  Stream.log

