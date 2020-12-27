#!/bin/bash
clear
raspivid -t 0 -h 800 -w 500 -fps 50 --flush -n -hf -b 50000000 -o - | gst-launch-1.0 -v fdsrc ! h264parse !  rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=192.168.43.169 port=5000
