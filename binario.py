import time

import pyautogui
pyautogui.PAUSE = 0.00
def linha():
    pyautogui.hotkey('Capslock')
    pyautogui.hotkey('scrolllock')
    pyautogui.hotkey('numlock')
    time.sleep(.1)
    pyautogui.hotkey('Capslock')
    pyautogui.hotkey('scrolllock')
    pyautogui.hotkey('numlock')
    time.sleep(.05)

def ponto():
    pyautogui.hotkey('Capslock')
    time.sleep(.1)
    pyautogui.hotkey('Capslock')
    time.sleep(.05)

def a():
    ponto()
    linha()

def b():
    linha()
    ponto()
    ponto()
    ponto()

def c():
    linha()
    ponto()
    linha()
    ponto()

def d():
    linha()
    ponto()
    ponto()

def e():
    ponto()

def f():
    ponto()
    ponto()
    linha()
    ponto()

def g():
    linha()
    linha()
    ponto()

def h():
    ponto()
    ponto()
    ponto()
    ponto()

def i():
    ponto()
    ponto()

def j():
    ponto()
    linha()
    linha()
    linha()

def k():
    linha()
    ponto()
    linha()

def l():
    ponto()
    linha()
    ponto()
    ponto()

def m():
    linha()
    linha()

def n():
    linha()
    ponto()

def o():
    linha()
    linha()
    linha()

def p():
    ponto()
    linha()
    linha()
    ponto()

def q():
    linha()
    ponto()
    linha()
    linha()

def r():
    ponto()
    linha()
    ponto()

def s():
    ponto()
    ponto()
    ponto()

def t():
    linha()

def u():
    ponto()
    ponto()
    linha()

def v():
    ponto()
    ponto()
    ponto()
    linha()

def w():
    ponto()
    linha()
    linha()

def x():
    linha()
    ponto()
    ponto()
    linha()

def y():
    linha()
    ponto()
    linha()
    linha()

def z():
    linha()
    linha()
    ponto()
    ponto()

def switch(letra):
    if letra == "a":
        a()
    elif letra == "b":
        b()
    elif letra == "c":
        c()
    elif letra == "d":
        d()
    elif letra == "e":
        e()
    elif letra == "f":
        f()
    elif letra == "g":
        g()
    elif letra == "h":
        h()
    elif letra == "i":
        i()
    elif letra == "j":
        j()
    elif letra == "k":
        k()
    elif letra == "l":
        l()
    elif letra == "m":
        m()
    elif letra == "n":
        n()
    elif letra == "o":
        o()
    elif letra == "p":
        p()
    elif letra == "q":
        q()
    elif letra == "r":
        r()
    elif letra == "s":
        s()
    elif letra == "t":
        t()
    elif letra == "u":
        u()
    elif letra == "v":
        v()
    elif letra == "w":
        w()
    elif letra == "x":
        x()
    elif letra == "y":
        y()
    elif letra == "z":
        z()
    elif letra == " ":
        time.sleep(.2)

frase = input("insita a frase")
for x in range(len(frase)):
    switch(frase[x].lower())


