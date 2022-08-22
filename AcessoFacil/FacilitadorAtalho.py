import glob
import os
import subprocess
from tkinter import *


def dummy():
    print(n.get())
    subprocess.check_call(n.get()+"\DATA005\\bin\\GesCooperAcessoRapido.exe")

master = Tk()

variable = StringVar(master)

files = glob.glob('D:/KB/GX9/*')
files.sort(key=os.path.getmtime, reverse=True)
print(files)
nomes = files
default = max(files)
variable.set(default)  # default value
n = StringVar(master)
n.set(default)

w = OptionMenu(master, n, *nomes)
w.pack()

dummy_b = Button(master, text='Dummy',command=dummy)
dummy_b.pack()

mainloop()
