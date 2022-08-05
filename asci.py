import pyautogui
from PIL import Image

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
Tk().withdraw()
filename = askopenfilename()
print(filename)
im = Image.open(filename) # Can be many different formats.
pix = im.load()
x,y = im.size  # Get the width and hight of the image for iterating over
f = open('readme.txt',"w")
f.truncate(0)
for w in range(0,y,3):
    for h in range(0,x,3):
        if pix[h,w] < (50, 50, 50, 255):
            print(' @ ', end='')
            f.write(' @ ')
        elif pix[h,w] < (100, 100, 100, 255):
            print(' % ', end='')
            f.write(' % ')
        elif pix[h,w] < (150, 150, 150, 255):
            print(' # ', end='')
            f.write(' # ')
        elif pix[h,w] < (200, 200, 200, 255):
            print(' * ', end='')
            f.write(' * ')
        else:
            print('   ', end='')
            f.write('   ')
    print("\n", end='')
    f.write("\n")
f.close()
