
def selecionacor(tupla):
    pyautogui.click(1097,93)
    time.sleep(2)
    for _ in range(7):
        pyautogui.hotkey('TAB')
    pyautogui.write(tupla(0))
    pyautogui.hotkey('TAB')
    pyautogui.write(tupla(1))
    pyautogui.hotkey('TAB')
    pyautogui.write(tupla(2))
    pyautogui.hotkey('ENTER')



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
pyautogui.PAUSE = 0.001
x,y = im.size  # Get the width and hight of the image for iterating over
xa = round(x/2)
ya = round(y/2)
for h in range(0,x,4):
    for w in range(0,y,4):
        selecionacor(pix[h,w])
        #pyautogui.click(h+sx-round(x/2),w+sy-round(y/2))
        time.sleep(100000)

