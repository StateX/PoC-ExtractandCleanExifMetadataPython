# -*- coding: utf-8 -*-

from pyexiv2 import ImageMetadata, ExifTag
metadata = ImageMetadata(raw_input("Foto: "))
metadata.read()

for item in metadata.exif_keys:
	tag = metadata[item]
	print tag
	f = open("Exifinfo.txt","a")
	f.write(str(tag) + "\n")
