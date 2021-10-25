# import colorgram
# import random
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
#
# import turtle as t
# import random
#
# screen = t.Screen()
# screen.title("Damian Hirst replica")
# screen.colormode(255)
#
#
# color_list = [
#     (131, 165, 204), (221, 149, 109), (30, 41, 62), (201, 134, 146), (166, 58, 48), (141, 184, 161),
#     (41, 104, 154), (236, 213, 94), (150, 59, 66), (215, 82, 71), (236, 165, 157), (51, 112, 91),
#     (33, 60, 55), (171, 29, 33), (156, 33, 30), (52, 44, 49), (229, 162, 166), (170, 188, 221),
#     (17, 96, 70), (57, 51, 48), (186, 101, 111), (30, 60, 110), (107, 126, 159), (174, 200, 188),
#     (34, 151, 210), (65, 66, 57)
# ]
#
# tim = t.Turtle()
# tim.shape('circle')
# tim.shapesize(1)
# tim.hideturtle()
# tim.penup()
#
# tim.setheading(225)
# tim.fd(300)
# tim.setheading(0)
#
#
# def move_forward():
#     for _ in range(10):
#         tim.fd(20)
#         tim.dot(20, random.choice(color_list))
#         tim.fd(20)
#
#
# for _ in range(5):
#     move_forward()
#     tim.left(90)
#     tim.fd(40)
#     tim.left(90)
#     move_forward()
#     tim.right(90)
#     tim.fd(40)
#     tim.right(90)
#
# screen = t.exitonclick()

# another way of solving it down below

import turtle as turtle_module
import random

screen = turtle_module.Screen()


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [
    (131, 165, 204), (221, 149, 109), (30, 41, 62), (201, 134, 146), (166, 58, 48), (141, 184, 161),
    (41, 104, 154), (236, 213, 94), (150, 59, 66), (215, 82, 71), (236, 165, 157), (51, 112, 91),
    (33, 60, 55), (171, 29, 33), (156, 33, 30), (52, 44, 49), (229, 162, 166), (170, 188, 221),
    (17, 96, 70), (57, 51, 48), (186, 101, 111), (30, 60, 110), (107, 126, 159), (174, 200, 188),
    (34, 151, 210), (65, 66, 57)
]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
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

screen = turtle_module.exitonclick()
