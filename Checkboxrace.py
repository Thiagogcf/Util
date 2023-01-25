import time
import pyautogui
pyautogui.PAUSE = .001

# define as dimensões da região de busca
region_size = (100, 300)

# encontra as coordenadas do centro da tela
screen_center = (pyautogui.size().width/2, pyautogui.size().height/2)

# encontra as coordenadas do canto superior esquerdo da região de busca
x1 = int(screen_center[0] - region_size[0]/2)
x2 = int(screen_center[0] + region_size[0]/2)
y1 = int(screen_center[1] - region_size[1]/2)
y2 = int(screen_center[1] + region_size[1]/2)



# define a região de busca
region = (x1, y1, x2, y2)
pyautogui.moveTo(x1,y1,duration = .2)
pyautogui.moveTo(x1,y2,duration = .2)
pyautogui.moveTo(x2,y2,duration = .2)
pyautogui.moveTo(x2,y2,duration = .2)
pyautogui.moveTo(x1,y1,duration = .2)
print(region)
for _ in range(100):
    try:
        check = pyautogui.locateCenterOnScreen('Img/Screenshot_4.png', confidence=.98)
        if(check!=None):
            pyautogui.click(check,duration = .1)
            print(check)
        else:
            print("Não achou")
    except:
        print("deu erro")

