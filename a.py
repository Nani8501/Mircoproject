from __future__ import print_function
import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import decode
import numpy as np
import cv2
import re
import webbrowser  
import qrcode as q
from PIL import Image as i
def reading():
  def cam():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    def decode(im) :
      decodedObjects = pyzbar.decode(im)
      for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data,'\n')     
      return decodedObjects
    font = cv2.FONT_HERSHEY_SIMPLEX
    while(cap.isOpened()):
      ret, frame = cap.read()
      im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      decodedObjects = decode(im)
      for decodedObject in decodedObjects: 
        points = decodedObject.polygon
        if len(points) > 4 : 
          hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
          hull = list(map(tuple, np.squeeze(hull)))
        else : 
          hull = points;
        n = len(hull)     
        for j in range(0,n):
          cv2.line(frame, hull[j], hull[ (j+1) % n], (255,0,0), 3)
        x = decodedObject.rect.left
        y = decodedObject.rect.top
        print(x, y)
        print('Type : ', decodedObject.type)
        print('Data : ', decodedObject.data,'\n')
        barCode = str(decodedObject.data)
        cv2.putText(frame, barCode, (x, y), font, 1, (0,255,255), 2, cv2.LINE_AA)
      cv2.imshow('frame',frame)
      key = cv2.waitKey(1)
      if key & 0xFF == ord('q'):
          break
      elif key & 0xFF == ord('s'):
          cv2.imwrite('Capture.png', frame)     
    img=cv2.imread('Capture.png')
    det=cv2.QRCodeDetector()
    val, pts, st_code=det.detectAndDecode(img)
    print(val)
    webbrowser.open(val)
    cap.release()
    cv2.destroyAllWindows()
  def photo():
    path=input("Enter path and name:")
    img=cv2.imread(path)
    det=cv2.QRCodeDetector()
    val, pts, st_code=det.detectAndDecode(img)
    print("\n"+val+"\n")
    webbrowser.open(val)
  c=input("choose c for Cam or p for photo for Decryption:")
  if c=="c":
    cam()
  elif c=='p':
    photo()
  else:
    print("Try Again")
def writing():
  data =input("Enter Data to be encript:")
  file = input("Enter name of the file:")
  image = q.make(data)
  file=file+".png"
  image.save(file)
  im = i.open(file)
  im.show()
m=input("choose e for Encription or d for photo for Decryption:")
if m=="e":
  writing()
elif m=='d':
  reading()
else:
  print("Try Again")