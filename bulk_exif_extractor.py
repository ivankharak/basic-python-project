#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry

import piexif
import csv
import os
from os import path

# //Fairly rudamentary. Barely any post-processing done.


def get_exif(_path):
    s = piexif.load(_path)
    d = {}
    thumbnail = s.pop("thumbnail")
    usercomment = s.get("Exif").get(37510)

    d["path"] = _path

    d["lat_ref_gps_1"] = s.get("GPS").get(1)
    d["lon_ref_gps_3"] = s.get("GPS").get(3)
    d["lat_gps_2"] = s.get("GPS").get(2)
    d["lon_gps_4"] = s.get("GPS").get(4)
    d["altitude_ref_gps_5"] = s.get("GPS").get(5)
    d["altitude_gps_6"] = s.get("GPS").get(6)
    d["tstamp_gps_7"] = s.get("GPS").get(7)
    d["datestamp_gps_29"] = s.get("GPS").get(29)

    d["make_271"] = s["0th"].get(271)
    d["model_272"] = s["0th"].get(272)
    d["orient_274"] = s["0th"].get(274)
    d["xres_282"] = s["0th"].get(282)
    d["yres_283"] = s["0th"].get(283)
    d["res_unit_296"] = s["0th"].get(296)
    d["software_305"] = s["0th"].get(305)
    d["datetime_306"] = s["0th"].get(306)
    d["ycbcr_positioning_531"] = s["0th"].get(531)
    d["exiftag_34665"] = s["0th"].get(34665)
    d["gpstag_34853"] = s["0th"].get(34853)

    d["exposure_time_33434"] = s["Exif"].get(33434)
    d["fnum_33437"] = s["Exif"].get(33437)
    d["exposure_program_34850"] = s["Exif"].get(34850)
    d["iso_34855"] = s["Exif"].get(34855)
    d["exif_version_36864"] = s["Exif"].get(36864)
    d["datetime_original_36867"] = s["Exif"].get(36867)
    d["shutterspeed_37377"] = s["Exif"].get(37377)
    d["aperture_37378"] = s["Exif"].get(37378)
    d["exposurebias_37380"] = s["Exif"].get(37380)
    d["meteringmode_37383"] = s["Exif"].get(37383)
    d["flash_37385"] = s["Exif"].get(37385)
    d["subsectime_37520"] = s["Exif"].get(37520)
    d["datetime_digitized_36868"] = s["Exif"].get(36868)
    d["subsectime_original_37521"] = s["Exif"].get(37521)
    d["subsectime_digitized_37522"] = s["Exif"].get(37522)
    d["colorspace_40961"] = s["Exif"].get(40961)
    d["pixel_x_dim_40962"] = s["Exif"].get(40962)
    d["pixel_y_dim_40963"] = s["Exif"].get(40963)
    d["focalplane_xres_41486"] = s["Exif"].get(41486)
    d["focalplane_yres_41487"] = s["Exif"].get(41487)
    d["scenecapturetype_41990"] = s["Exif"].get(41990)

    d["compression_259"] = s["1st"].get(259)
    return d


def img_list(_path):
    for root, _, files in os.walk(_path):
        for name in files:
            if path.splitext(path.join(root, name))[1] in [".jpeg", ".jpg", ".tiff"]:
                yield path.join(root, name)


def export(data):
    file_exists = path.isfile("exif.csv")

    with open("exif.csv", "a") as f:
        print(data)
        fieldnames = data.keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)


if __name__ == "__main__":
    dir_path = input("DIR PATH: ")
    img_paths = img_list(dir_path)

    for img in img_paths:
        try:
            export(get_exif(img))
        except:
            continue
