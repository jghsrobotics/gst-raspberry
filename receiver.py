import os
import sys

## Intended for use on a Linux machine
TCPcommand = "gst-launch-1.0 -v tcpclientsrc host={0} port={1} ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false"
UDPcommand = "gst-launch-1.0 -e -v udpsrc port={0} ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! fpsdisplaysink sync=false text-overlay=false"

ip_address = "192.168.43.169"
port = "5000"
TCP = False

for index, item in enumerate(sys.argv):
    if item == "-T":
        TCP = True

    if item == "-U":
        TCP = False

    if "host=" in item:
        ip_address = item.split("=")[-1]

    if "port=" in item:
        port = item.split("=")[-1]



if TCP:
    print("Trying to receive TCP pipe...")
    os.system(TCPcommand.format(ip_address, port))
else:
    print("Trying to receive UDP pipe...")
    os.system(UDPcommand.format(port))

