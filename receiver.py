import os

## Intended for use on a Linux machine
command = "gst-launch-1.0 -v tcpclientsrc host={0} port={1} ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false"

ip_address = "192.168.43.169"
port = "5000"
protocol = "tcpclientsrc"

UDP = False

if UDP:
    protocol = "udpsrc"

os.system(command.format(ip_address, port))

