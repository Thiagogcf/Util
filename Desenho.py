import time

import pyautogui
from PIL import Image

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()
print(filename)
im = Image.open(filename) # Can be many different formats.
pix = im.load()
pyautogui.PAUSE = 0.001
x,y = im.size  # Get the width and hight of the image for iterating over
for h in range(0,x,3):
    for w in range(0,y,3):
        if pix[h,w] < (100, 100, 100, 255):
            #pyautogui.moveTo(h+100,w+100)
            pyautogui.click(h+300,w+300)
            print(pix[h,w])  # Get the RGBA Value of the a pixel of an image