from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("DarkOrange2")

'''
for _ in range(4):
    tim.forward(100)
    tim.right(90)

tim.forward(100)

for _ in range(5):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

for _ in range(3):
    tim.right(360/3)
    tim.forward(100)
for _ in range(4):
    tim.pencolor("red")
    tim.right(90)
    tim.forward(100)
for _ in range(5):
    tim.pencolor("blue")
    tim.right(360/5)
    tim.forward(100)
for _ in range(6):
    tim.pencolor("black")
    tim.right(360/6)
    tim.forward(100)
for _ in range(8):
    tim.pencolor("purple")
    tim.right(360/8)
    tim.forward(100)
'''

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.pencolor(random.choice(colours))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()