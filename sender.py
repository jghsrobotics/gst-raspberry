import os
import sys

UDPcommand = "raspivid -n -t 0 -w {0} -h {1} -fps {2} {3} -b {4} -o - | gst-launch-1.0 -e -vvvv fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! udpsink host={5} port={6}"
TCPcommand = "raspivid -n -t 0 -w {0} -h {1} -fps {2} {3} -b {4} -o - | gst-launch-1.0 -v fdsrc ! h264parse !  rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host={5} port={6}"

height = 800
width = 500
FPS = 50
bitrate = "50000000"
extraOptions = "--flush -hf -vf"

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
    print("Trying to send through TCP pipe...")
    os.system(TCPcommand.format(width, height, FPS, extraOptions, bitrate, ip_address, port))

else:
    print("Trying to send through UDP pipe...")
    os.system(UDPcommand.format(width, height, FPS, extraOptions, bitrate, ip_address, port))











