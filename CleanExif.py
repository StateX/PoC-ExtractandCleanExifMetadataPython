# -*- coding: utf-8 -*-
from PIL import Image
import os

d1= raw_input ("Foto: ")
d2 = os.path.splitext(d1)[1]
try: 
	foto = Image.open(d1)
	foto.save("copiasinmeta"+ d2)
except: 
	print d2,"No soportado"	