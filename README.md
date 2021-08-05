# RaspberryPiCam

These are python scripts dedicated to providing ultra low-latency streaming of a Raspberry Pi Camera Module across a LAN. 

## Prerequisites
* [Gstreamer](https://gstreamer.freedesktop.org/documentation/installing/index.html?gi-language=c) - You will need to install the command line version of GStreamer on both sides for this to work, as this simply runs bash commands.

* Python 3. Once installed, run `python3 -m pip install -r requirements.txt`

* Any Linux Computer (This might work with Windows or mac if `gst-launch-1.0` is accessible from the command line; See `receiver.py`)

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
  // The sender should point to the receiver's IP address, and vise versa. (str)

  # Public IP Address
  // This machine's public IP address. (str)

  # Port
  // Number of the port you're using (uint)

  # Protocol (UDP / TCP)
  // Use the 'UDP' or 'TCP' protocol by simply typing either one
  
  # Receiver OS (Windows / Linux)
  // Use the 'Windows' or 'Linux' to determine how gst-launcher-1.0 is called. 
  // For windows, makes sure you use the MSVC 64-bit Development Installer. 

  ## SENDER ONLY ---------------------------

  # Height
  // Height of the video feed in pixels (int)

  # Width
  // Width of the video feed in pixels (int)

  # FPS
  // FPS of the video feed. Anything greater than 30 FPS is zoomed in (int)

  # Bitrate
  // Allowed bitrate in bits. This should be as high as possible for super low-latency, though if you go too high it'll integer overflow. 
  // On the raspberry pi, the max bitrate is 25 mbs, which would be `20000000` in this setting. (uint)
  ```

## Making it fast
From experience, messing with these will reduce latency:
* Lowering resolution via `Height` and `Width`
* Increasing bitrate
* Increasing FPS
* Lowering FPS if bandwidth is exceeded
* Lowering `-q` manually in `sender.py` (0 - 70)
* Using UDP instead of TCP
* Using a 5ghz router or hotspot between the machines
* Connecting router to Linux machine via ethernet 


## Troubleshooting

*Why is the camera zoomed in?*

The Raspberry Pi Camera module will zoom in if the FPS is above around 30. To make the camera zoomed out, set it to an FPS of ~30 or lower

*Why is the video literal seconds behind the video feed?*

If the resolution or FPS is too high, your router will actually buffer frames before sending them out to not go over its bandwidth. Over time, this may result in a "traffic jam" that will cause your video feed to lag far behind.

*More to come*










