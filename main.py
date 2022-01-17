import random
import string
import glob
import os

from PIL import Image
import requests

name = input('What Face? ') #py -m nuitka --lto=no main.py | For Installing to exe
pack_type = input('What Pack type (example : 16 , 128)')

pathy = input('Path to resource pack folder(Replace the \ with /): ')
path = pathy + '/*.png'
r = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")
rdata = r.json()
uuid = rdata["id"]
names = rdata["name"]
req = requests.get(f"https://visage.surgeplay.com/face/{pack_type}/{uuid}")
with open("face.png","wb") as f:
    f.write(req.content)
for file in glob.glob(path):
    img = Image.open(file)
    img2 = Image.open('face.png')
    img2.paste(img,(0,0))
    img2.save(file)
