import glob
import cv2
import pandas as pd
import pathlib
import qrcode as q
from PIL import Image as i
data =input("Enter Data to be encript:")
file = input("Enter name of the file:")
image = q.make(data)
file=file+".png"
image.save(file)
im = i.open(file)
im.show()