from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.uix.camera import Camera
from kivy.lang import Builder
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

Builder.load_file("myapplayout.kv")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FPS, 30.0)

font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        # print("Data", obj.data)
        cv2.putText(frame, str(obj.data), (50, 50), font, 2, (255, 0, 0), 3)
        print(str(obj.data))
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27: break
    if (key & 0xFF == ord('c')):
        print(str(obj.data))

