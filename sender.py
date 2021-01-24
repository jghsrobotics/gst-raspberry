import os
import sys
from PythonFileLibrary.src.FileReader import *

## Read from configuration file first
configFile = FileReader('config')

def GetSetting(fileReader : FileReader, setting : str):
    fileReader.ResetCursor()

    for line in configFile:
        line = line.strip()
        if setting in line:
            fileReader.MoveCursorDown()
            line = fileReader.GetCurrentLine().strip()
            return line
    
    return None

remoteIP = GetSetting(configFile,   '# Remote Public IP Address')
localIP = GetSetting(configFile,    '# Public IP Address')
port = GetSetting(configFile,       '# Port')
protocol = GetSetting(configFile,   '# Protocol (UDP / TCP)')
height = GetSetting(configFile,     '# Height')
width = GetSetting(configFile,      '# Width')
FPS = GetSetting(configFile,        '# FPS')
bitrate = GetSetting(configFile,    '# Bitrate')

UDPcommand = "raspivid -n -t 0 -w {0} -h {1} -qp 40 -fps {2} --flush -b {3} -o - | gst-launch-1.0 -e -vvvv fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! udpsink host={4} port={5}"
TCPcommand = "raspivid -n -t 0 -w {0} -h {1} -qp 40 -fps {2} --flush -b {3} -o - | gst-launch-1.0 -v fdsrc ! h264parse !  rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host={4} port={5}"


if protocol == "TCP":
    print("Trying to send through TCP pipe...")
    os.system(TCPcommand.format(width, height, FPS, bitrate, localIP, port))

elif protocol == "UDP":
    print("Trying to send through UDP pipe...")
    os.system(UDPcommand.format(width, height, FPS, bitrate, remoteIP, port))











