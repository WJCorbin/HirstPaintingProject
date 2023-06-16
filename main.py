# from colorgram import extract
#
# colors = extract("DamienHirstPainting.png", 30)
# color_list = []
#
# for color in colors:
#     color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(color_list)
# Painting is 10 X 10
# Dot size is 20
# Space between dots is 50
import turtle as t
import random as r

color_list = [
    (204, 161, 114), (150, 87, 52), (142, 169, 184), (42, 105, 133), (203, 154, 22), (194, 148, 161),
    (220, 200, 139), (148, 18, 56), (20, 49, 73), (143, 68, 86), (141, 169, 157), (59, 39, 33), (61, 32, 50),
    (193, 101, 76), (186, 91, 114), (67, 111, 86), (6, 84, 110), (10, 60, 49), (109, 44, 35), (218, 176, 187),
    (14, 90, 74), (216, 180, 173), (74, 149, 166), (171, 199, 207), (113, 124, 150), (181, 198, 190)
]
tim = t.Turtle()
screen = t.Screen()
tim.hideturtle()
tim.speed(0)
t.colormode(255)
tim.penup()
x = -225
y = -225
for height in range(10):
    tim.setposition(x, y)
    for width in range(10):
        tim.dot(20, r.choice(color_list))
        tim.forward(50)
    y += 50

screen.exitonclick()
