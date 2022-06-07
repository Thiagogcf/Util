import time

import pyautogui
from PIL import Image
time.sleep(5)
im = Image.open('Img\Screenshot_1.png') # Can be many different formats.
pix = im.load()
pyautogui.PAUSE = 0
x,y = im.size  # Get the width and hight of the image for iterating over
for h in range(x):
    for w in range(y):
        if pix[h,w] < (200, 200, 200, 255):
            #pyautogui.moveTo(h+100,w+100)
            pyautogui.click(h+100,w+100)
            print(pix[h,w])  # Get the RGBA Value of the a pixel of an image
