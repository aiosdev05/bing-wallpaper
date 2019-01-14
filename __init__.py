"""
Author: Brian Wing
Version: 2019.1.13
License: Apache 2.0
Description: This script is used to download the day's image from bing.com and set it as the dekstop wallpaper.
"""

import urllib.request
import json
import ctypes
from pathlib import Path
import os
import getpass

base_url = "https://www.bing.com/"
json_url = "HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"  # This is the address where Bing keeps the info for its images
img_url = ""
img_name = ""
save_loc = "C:\\Users\\" + getpass.getuser() + "\\Pictures\\Bing Backgrounds\\"

print("Finding today's image...")

# Get JSON info about what the path the image for today is
with urllib.request.urlopen(base_url + json_url) as url:
    data = json.loads(url.read().decode())
    img_url = data["images"][0]["url"]  # Get today's image url postfix. This should be something like /az/hprichbg/rb/GBRBday_EN-US12873687095_1920x1080.jpg
    img_url_pieces = img_url.split("/")
    img_name = img_url_pieces[len(img_url_pieces) - 1]  # The name of the image is the last part of the img_url

background_folder = Path(save_loc)
if not background_folder.exists():
    print("Creating backgrounds folder at \"" + str(background_folder) + "\"...")
    os.makedirs(background_folder)  # background_folder doesn't exists, create it

print("Downloading image...")
urllib.request.urlretrieve(base_url + img_url, save_loc + img_name)  # Download img from Bing and save in save location

print("Setting image as background...")
ctypes.windll.user32.SystemParametersInfoW(20, 0, save_loc + img_name, 0)  # Set the downloaded image as the wallpaper

print("Complete")
exit(0)
