import numpy as np
from PIL import Image
from tkinter import Tk, filedialog

Tk().withdraw()
filename = filedialog.askopenfilename()

im = Image.open(filename)
im.thumbnail((120, 120))
im = np.array(im)
x, y, _ = im.shape

lookup = [
    (0, 0, 0, '@'),
    (25, 25, 25, 'B'),
    (50, 50, 50, '%'),
    (75, 75, 75, '&'),
    (100, 100, 100, '#'),
    (125, 125, 125, 'X'),
    (150, 150, 150, '*'),
    (175, 175, 175, '+'),
    (200, 200, 200, ';'),
    (225, 225, 225, ':'),
    (250, 250, 250, '.'),
    (255, 255, 255, ' '),
]

def find_closest(pixel):
    return min(lookup, key=lambda c: sum((c[i] - pixel[i]) ** 2 for i in range(3)))

with open('readme.txt', 'w') as f:
    for row in range(0, y, 1):
        line = ''.join(find_closest(tuple(im[row, col]))[3] for col in range(0, min(x, y), 2))
        print(line)
        f.write(line + '\n')
