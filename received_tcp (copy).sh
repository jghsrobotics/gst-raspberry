#!/bin/bash
clear

gst-launch-1.0 -v tcpclientsrc host=192.168.43.169  port=5000 ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false
