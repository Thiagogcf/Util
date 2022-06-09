import time

import pyautogui
from PIL import Image
im = Image.open('Img\Screenshot_2.png') # Can be many different formats.
pix = im.load()
pyautogui.PAUSE = 0.001
x,y = im.size  # Get the width and hight of the image for iterating over
for h in range(0,x,1):
    for w in range(0,y,1):
        if pix[h,w] < (100, 100, 100, 255):
            #pyautogui.moveTo(h+100,w+100)
            pyautogui.click(h+300,w+300)
            print(pix[h,w])  # Get the RGBA Value of the a pixel of an image 