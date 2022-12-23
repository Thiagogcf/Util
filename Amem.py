import math
import pyautogui

def get_shape_vertices(sides, size=100):
    vertices = []
    angle = 360 / sides
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width / 2, screen_height / 2
    for i in range(sides):
        x = size * math.cos(math.radians(angle * i)) + center_x
        y = size * math.sin(math.radians(angle * i)) + center_y
        vertices.append((x, y))
    return vertices

print(get_shape_vertices(3))  # triangle
x = get_shape_vertices(7)

pyautogui.moveTo(x[0])
pyautogui.mouseDown()
for y in x:
    pyautogui.moveTo(y,duration=.25)
    for z in x:
        pyautogui.moveTo(y, duration=.1)
        pyautogui.moveTo(z, duration=.1)

pyautogui.mouseUp()
