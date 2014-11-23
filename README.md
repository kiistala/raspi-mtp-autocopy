# raspi-mtp-autocopy
Scripts for Raspberry Pi to automate file copying from mobile devices

## Setup your Raspbian
Download an image from http://www.raspberrypi.org/downloads/

I used 2014-09-09-wheezy-raspbian.img

Write the image to an SD card. See http://www.raspberrypi.org/documentation/installation/installing-images/linux.md

### First boot
* Take all the space in the SD card to use
* Set a password
* Set your keyboard layout
* Allow SSH connections

## Second boot
Setup your network.

After you have got your system to connect to a network at boot, you can login with SSH and there's no need for display nor keyboard anymore.

### Install packages

Install support for MTP:

```
sudo apt-get install mtp-tools mtpfs
```

Upgrade system packages to latest package versions (this might take 10 minutes)

```
sudo apt-get update
sudo apt-get upgrade
```

### Set udev rules

First, find out the vendor and product IDs of the devices you want to connect to your RasPi and copy files automatically.

```
# E.g.
sudo mtp-detect

# This might reveal the IDs, too:
lsusb
```
I'm using Samsung Tab 3:
IdVendor: 04e8
IdProduct: 6860

When you have the IDs, add a udev rule. My command was:
```
sudo bash -c "echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="04e8", ATTR{idProduct}=="6860", MODE="0666"' > /etc/udev/rules.d/51-android.rules"

# Restart USB services
sudo service udev restart
```

### Configure fuse

Modify /etc/fuse.conf:

```
# This uncomments a line beginning with "user_allow_other"
sudo sed -i 's/^#user_allow_other/user_allow_other/' /etc/fuse.conf
```

### Add a mount point

```
sudo mkdir /media/SamsungTab3
sudo chmod a+rwx /media/SamsungTab3

# This should add user "pi" to "fuse" group
sudo adduser $USER fuse
```

## Setup the Auto Copy

tbd


-----

## Sources
udev rule, mtpfs: http://www.omgubuntu.co.uk/2011/12/how-to-connect-your-android-ice-cream-sandwich-phone-to-ubuntu-for-file-access

