#! /usr/bin/env python3

"""
Author: Brian Wing
Version: 2020.9.6.1
License: Apache 2.0
Description: This script is used to download the day's image from bing.com and set it as the desktop wallpaper on Windows.
"""

from os import makedirs
from os.path import join
from pathlib import Path
from urllib import request
from urllib.error import URLError
from json import loads
from ctypes import windll

if __name__ == "__main__":
    base_url = "https://www.bing.com/"
    json_url = "HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"  # This is the address where Bing keeps the info for its images.
    img_url = ""
    img_name = ""
    save_loc = join(Path.home(), "Pictures", "Bing Backgrounds")

    print("Finding today's image...")

    # Get JSON info about what the path the image for today is.
    try:
        with request.urlopen(base_url + json_url) as url:
            data = loads(url.read().decode())
            img_url = data["images"][0][
                "url"]  # Get today's image url postfix. This should be something like /th?id=OHR.GrapeHarvest_EN-US9833740254_1920x1080.jpg&rf=NorthMale_1920x1080.jpg&pid=hp
            img_url_pieces = img_url.split("&")
            img_name = img_url_pieces[len(img_url_pieces) - 2].split("=")[1]  # The name of the image comes after rf=
    except URLError as e:
        print("Failed to find image:\n{}".format(e))
        exit(1)

    background_folder = Path(save_loc)
    if not background_folder.exists():
        print("Creating backgrounds folder at \"" + save_loc + "\"...")
        makedirs(background_folder)  # background_folder doesn't exists, create it

    print("Downloading image...")
    request.urlretrieve(base_url + img_url,
                        join(save_loc, img_name))  # Download img from Bing and save in save location.

    print("Setting image as background...")
    windll.user32.SystemParametersInfoW(20, 0, join(save_loc, img_name), 0)  # Set the downloaded image as the wallpaper.

    print("Complete")
    exit(0)
