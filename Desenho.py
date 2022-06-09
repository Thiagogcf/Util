import time
import pyautogui
from PIL import Image

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
sx,sy = pyautogui.size()
sx= round(sx/2)
sy= round(sy/2)
print(sx,sy)
# Tk().withdraw()
# filename = askopenfilename()
filename = 'Img/Screenshot_2.png'
print(filename)
im = Image.open(filename) # Can be many different formats.
pix = im.load()
pyautogui.PAUSE = 0.00
x,y = im.size  # Get the width and hight of the image for iterating over
for h in range(1,x,1):
    for w in range(1,y,1):
        if pix[h,w] < (69, 69, 69, 255):
            pyautogui.moveTo(h+sx-round(x/2),w+sy-round(y/2))
            print(((h*w)/(x*y))*100)
            #pyautogui.click(h+300,w+300)
            #print(pix[h,w])  # Get the RGBA Value of the a pixel of an image