import turtle
from PIL import Image

# open the image using the Pillow library
image = Image.open('Img/Screenshot_1.png')

# convert the image to grayscale
image = image.convert('L')

# create a turtle object
t = turtle.Turtle()

# define the size of the image
size = 200

# move the turtle to the starting position
t.penup()
t.goto(-size/2, size/2)
t.pendown()

# iterate over the pixels in the image
for y in range(image.height):
    for x in range(image.width):
        # get the pixel value at (x, y)
        pixel = image.getpixel((x, y))

        # set the pen color based on the pixel value
        t.pencolor(pixel/255, pixel/255, pixel/255)

        # draw a line based on the pixel value
        t.forward(1)

# hide the turtle
t.hideturtle()

# keep the window open until the user closes it
turtle.exitonclick()
