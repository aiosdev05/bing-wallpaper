"""
Author: Brian Wing
Version: 2018.6.11.1
License: Apache
"""

import urllib.request
import json
import ctypes

base_url = "https://www.bing.com/"
json_url = "HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"  # This is the address where Bing keeps the info for its images
img_url = ""
img_name = ""
save_loc = "C:\\Users\\Brian\\Pictures\\Bing Backgrounds\\"

# Get JSON info about what the path the image for today is
with urllib.request.urlopen(base_url + json_url) as url:
    data = json.loads(url.read().decode())
    img_url = data["images"][0]["url"]  # Get today's image url postfix. This should be something like /az/hprichbg/rb/GBRBday_EN-US12873687095_1920x1080.jpg
    img_url_pieces = img_url.split("/")
    img_name = img_url_pieces[len(img_url_pieces) - 1]  # The name of the image is the last part of the img_url

urllib.request.urlretrieve(base_url + img_url, save_loc + img_name)  # Download img from Bing and save in save location
ctypes.windll.user32.SystemParametersInfoW(20, 0, save_loc + img_name, 0)  # Set the downloaded image as the wallpaper

exit(0)
