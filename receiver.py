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
osType = GetSetting(configFile,         '# Receiver OS (Windows / Linux)')

## Run commands.
TCPcommand = "gst-launch-1.0 -v tcpclientsrc host={0} port={1} ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false"
UDPcommand = "gst-launch-1.0 -e -v udpsrc address={0} port={1} ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! autovideosink sync=false"

if osType == 'Windows':
    TCPcommand = r"C:\gstreamer\1.0\msvc_x86_64\bin\gst-launch-1.0.exe -v tcpclientsrc host={0} port={1} ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false"
    UDPcommand = r"C:\gstreamer\1.0\msvc_x86_64\bin\gst-launch-1.0.exe -e -v udpsrc address={0} port={1} ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! autovideosink sync=false"

if protocol == "TCP":
    print("Trying to receive from TCP pipe...")
    os.system(TCPcommand.format(remoteIP, port))

elif protocol == "UDP":
    # NOTE: Make sure server has its external IP address pointed to this computer
    print("Trying to receive UDP pipe...")
    os.system(UDPcommand.format(localIP, port))
