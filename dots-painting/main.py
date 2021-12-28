
"""
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

"""
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(184, 130, 158), (143, 78, 113), (211, 157, 97), (137, 158, 184), (166, 104, 137), (54, 102, 139), (145, 13, 44), (1, 0, 0), (202, 207, 219), (10, 54, 93), (120, 110, 75), (220, 205, 215), (76, 112, 96), (54, 12, 33), (116, 120, 155), (158, 140, 79), (29, 63, 109), (226, 206, 193), (210, 179, 193), (182, 188, 209), (142, 158, 147), (68, 145, 178), (9, 79, 112), (6, 14, 11), (231, 193, 118), (107, 140, 118), (174, 108, 97), (221, 177, 168), (30, 86, 79), (207, 215, 213)]

tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.hideturtle()
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
