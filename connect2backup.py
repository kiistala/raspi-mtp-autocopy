#!/usr/bin/env python

#     Copyright 2015 Ilkka Kiistala <ilkkakiistala@gmail.com>
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#             http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

import os
import glib
import gudev
import sys
import pprint
import sys

__version__ = "0.0.1"
__author__  = "Ilkka Kiistala <ilkkakiistala@gmail.com>"

class Main:
    def __init__(self):

        while True:
            result = self.watch_added_device()

            if result:
                print "A device was added"
                # os.system("echo '1' >> /home/pi/c2b.log")
                os.system("/bin/bash /home/pi/copier.sh >> /home/pi/copier.log")

    def watch_added_device(self):
        loop = glib.MainLoop()
        device_listener = DeviceListener(self, loop, "add")

        client = gudev.Client(["usb/usb_device"])
        # client = gudev.Client([]) # all types

        client.connect("uevent", device_listener.callback, None)

        loop.run()
        return device_listener.device_found

class DeviceListener:
    def __init__(self,app,loop,event):
        self.loop = loop
        self.app = app
        self.event = event
        self.device_info = {}

    def callback(self, client, action, device, user_data):
        # e.g. 04e8
        device_vendor_id = device.get_property("ID_VENDOR_ID")
        # e.g. 6860
        device_model_id = device.get_property("ID_MODEL_ID")

        # device_product = device.get_property("ID_PRODUCT_ID")
        # device_serial = device.get_property("ID_SERIAL")
        # print "{}, {}\n{}".format(action, [device_vendor_id, device_model_id])

        if action == "add":
            print "add detected: {}:{}".format(device_vendor_id, device_model_id)

            # Samsung Tab 3:
            if device_vendor_id == "04e8" and device_model_id == "6860":
                print "Tab3 detected"
                self.loop.quit()
                self.device_found = True
                return self.device_found

app = Main()
