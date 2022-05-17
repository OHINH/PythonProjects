import colorgram

rgb_colors = []
colors = colorgram.extract('IntermediateProjects\Turtle_class_final\Kirbycolor.jpg', 36)


for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    rgb_colors.append((r, g, b))


import turtle as tl
import random

image_colors = [(189, 221, 247), (130, 171, 209), (245, 236, 211), (159, 184, 246), (137, 66, 109), (191, 247, 244), (79, 93, 128), (222, 119, 172), (213, 71, 147), (147, 14, 72), (235, 207, 224), (210, 152, 104), (233, 163, 208), (52, 42, 119), (83, 20, 42), (152, 80, 44), (24, 25, 79), (104, 114, 174), (241, 211, 113), (123, 212, 249), (84, 21, 14), (244, 164, 152), (189, 129, 52), (136, 27, 13), (205, 91, 69), (151, 175, 160), (92, 139, 155), (81, 117, 90), (33, 74, 90), (164, 208, 193)]

tl.colormode(255)

Hirst = tl.Turtle()
Hirst.shape('turtle')
Hirst.hideturtle()
Hirst.penup()
Hirst.speed(0)
for i in range(30):
    Hirst.goto(-290,250-i*20)
    for j in range(30):
        Hirst.dot(10,random.choice(image_colors))
        Hirst.forward(20)


screen = tl.Screen()
screen.screensize(500,500)
screen.exitonclick()