# Marquee Tee
## Tom's Hardware <> Stephen Hawes  

![Demo Gif](https://github.com/sphawes/ledTshirt/raw/master/demoGif.gif)

Welcome to the software guide for the Marquee Tee! This will also serve as a repositiory for all code needed to get up and running.

### Arduino  
Go ahead and install the [latest stable version](https://www.arduino.cc/en/main/software) of the Arduino IDE on your computer. Then [download the git repository](https://github.com/sphawes/ledTshirt/archive/master.zip), and in "scrollWhenRead" find the Arduino sketch (called scrollWhenRead.ino) that interprets the data coming from the Raspberry Pi.  

Next, connect your Arduino to your computer with a USB cable and upload the sketch! After uploading successfully, the Arduino will be able to interpret the signals from the Raspberry Pi and convert them into signals for the Neopixel panels.


### Raspberry Pi
Grab a Raspberry Pi with built-in Wifi capabilities (or an older version and a Wifi dongle). Next, load a fresh version of Raspbian onto a micro SD card with at least 8GB of storage. The official guide for doing that is [here](https://www.raspberrypi.org/documentation/installation/installing-images/).

Once you install your operating system and plug the SD card into the Pi, go ahead and connect a keyboard, an HDMI monitor, and power it through the Micro USB jack. When your Pi boots and you get a command line prompt, type the following commands in, hitting enter after every line and waiting to enter the next until you're given another command prompt:

```
git clone https://github.com/sphawes/ledTshirt.git
pip3 install feedparser
pip3 install pyserial
```
Awesome! Everything should now be installed! Running `python3 ledTshirt/sendText/sendText.py` will run the script that talks to tomshardware.com, gets the most recent titles, and sends them through a USB port to the Arduino. If you want to change what data is displayed, enter `nano ledTshirt/sendText/sendText.py` to make changes to the script.  

Now that the script is all set to go, we need to make the Pi automatically run it on boot. We'll do this by making what's called a "service." You've already downloaded all the configurations for making this service, you just have to move them to the right place. Do this with:

```
cd ~/ledTshirt
sudo cp tshirt.service /etc/systemd/system/myscript.service
```

This might prompt you for a password; just type in "raspberry" which is the default Raspbery Pi password. Now that your configuration file is in the right place, you can start the service with the following command:  

```
sudo systemctl start tshirt.service
```

Now the main script will run when you reboot your Pi! Awesome. But first we need to connect the Pi to wifi. Connecting to wifi is easier from the GUI. Start XFCE with this:

```
startx
```
Then click on the network icon in the upper right and connect. I recommend setting it up to connect to your phone's wifi hotspot so you can use the shirt on the go!
