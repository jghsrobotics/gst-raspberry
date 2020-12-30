# RaspberryPiCam

These are python scripts dedicated to providing ultra low-latency streaming of a Raspberry Pi Camera Module across a LAN. 

## Prerequisites
* [Gstreamer](https://gstreamer.freedesktop.org/documentation/installing/index.html?gi-language=c) - You will need to install the command line version of GStreamer on both sides for this to work, as this simply runs bash commands.

* Any Linux Computer (This might work with Windows or mac if `gst-launch-1.0` is accessible from the command line)

* Raspberry Pi 4 (Lower versions of Pi should have a WiFi card)

* Raspberry Pi Camera Module V2 (This might work with V1 if raspivid works with it)

* Dedicated Router - The key to ultra low-latency streaming is bandwidth, so having a dedicated LAN via a internet-less router is crucial. I use personally use a 5Ghz hotspot.

## Running
Running these scripts is super simple. First, make sure the Linux Computer and Raspberry Pi are connected to the same LAN. Then on the Raspberry Pi, run `sender.py` via Python 3+, and on the Linux Computer, run `receiver.py`. Personally, I run these commands via the command line, with the Raspberry Pi being controlled via a SSH tunnel.

## Configuring
The stream can be configured by editing `config` before running either of them. Here's a breakdown of what they do:

  ```
  # Remote Public IP Address
  // The IP address of the device you are receiving from / sending to.
  // The sender should point to the receiver's IP address, and vise versa. 

  # Public IP Address
  // This machine's public IP address. 

  # Port
  // Number of the port you're using

  # Protocol (UDP / TCP)
  // Use the 'UDP' or 'TCP' protocol by simply typing either one

  ## SENDER ONLY ---------------------------

  # Height
  // Height of the video feed in pixels

  # Width
  // Width of the video feed in pixels

  # FPS
  // FPS of the video feed

  # Bitrate
  // Allowed bitrate in bits. This should be as high as possible for super low-latency, though if you go too high it'll integer overflow. 
  // On the raspberry pi, the max bitrate is 25 mbs, which would be `20000000` in this setting.
  ```










