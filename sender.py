import os

command = "raspivid -t 0 -h {0} -w {1} -fps {2} -n {3} -b {4} -o - | gst-launch-1.0 -v fdsrc ! h264parse !  rtph264pay config-interval=1 pt=96 ! gdppay ! {5} host={6} port={7}"
extraOptions = ""

height = 800
width = 500
FPS = 50
flush = True
horizontalFlip = True
verticalFlip = False
bitrate = "50000000"

ip_address = "192.168.43.169"
port = "5000"
protocol = "tcpserversink"

UDP = False

if UDP:
    protocol = "udpsink"

if flush:
    extraOptions += "--flush "

if horizontalFlip:
    extraOptions += "-hf "

if verticalFlip:
    extraOptions += "-vf "


os.system(command.format(height, width, FPS, extraOptions, bitrate, protocol, ip_address, port))









