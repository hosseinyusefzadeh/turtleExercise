# import turtle
# from turtle import Turtle, Screen
# import random
# import colorgram

################exersice one#################

# hossein_the_turtle = Turtle()
# screen = Screen()
# hossein_the_turtle.right(90)
# hossein_the_turtle.forward(100)
# hossein_the_turtle.right(90)
# hossein_the_turtle.forward(100)
# hossein_the_turtle.right(90)
# hossein_the_turtle.forward(100)
# hossein_the_turtle.right(90)
# hossein_the_turtle.forward(100)
# screen.exitonclick()


#########dash line############

# for i in range(20):
#     hossein_the_turtle.forward(5)
#     hossein_the_turtle.penup()
#     hossein_the_turtle.forward(5)
#     hossein_the_turtle.pendown()


#########triangle#############

##############Number1#############

# for i in range(3):
#     hossein_the_turtle.forward(90)
#     hossein_the_turtle.right(120)
#
#
# for i in range(4):
#     hossein_the_turtle.color("green")
#     hossein_the_turtle.forward(90)
#     hossein_the_turtle.right(90)
#
# for i in range(5):
#     hossein_the_turtle.color("yellow")
#     hossein_the_turtle.forward(90)
#     hossein_the_turtle.right(72)
#
# for i in range (6):
#     hossein_the_turtle.color("blue")
#     hossein_the_turtle.forward(90)
#     hossein_the_turtle.right(60)
#
# for i in range(7):
#     hossein_the_turtle.color("red")
#     hossein_the_turtle.forward(90)
#     hossein_the_turtle.right(51.5)
#
# screen = Screen()
# screen.exitonclick()



#############Number2#################

# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colors = (r,g,b)
#     return colors
#
# colors = ["medium aquamarine", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# def draw_shape(num_side):
#     angle = 360 / num_side
#     for _ in range(num_side):
#         hossein_the_turtle.forward(90)
#         hossein_the_turtle.right(angle)
#
# for shape_side_n in range(3,11):
#     hossein_the_turtle.color(random_color())
#     draw_shape(shape_side_n)




##################random Walk#################
# direction = [0, 90, 180, 270]
# colors = ["medium aquamarine", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# hossein_the_turtle.pensize(15)
# hossein_the_turtle.speed("fastest")
#
# for _ in range (200):
#     hossein_the_turtle.color(random.choice(colors))
#     hossein_the_turtle.forward(30)
#     hossein_the_turtle.setheading(random.choice(direction))





#############make a spirograph################

# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colors = (r, g, b)
#     return colors
#
#
# hossein_the_turtle.speed("fastest")
# def spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         hossein_the_turtle.color(random_color())
#         hossein_the_turtle.circle(100)
#         hossein_the_turtle.setheading(hossein_the_turtle.heading() + size_of_gap)
#
#
# spirograph(3)
# screen = hossein_the_turtle.Screen()
# screen.exitonclick()


########### below we using colorgram to extract image colors ##############

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)




##################painting###########################

# hossein_the_turtle.penup()
# turtle.colormode(255)
# color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
#
#
# hossein_the_turtle.speed("fastest")
# hossein_the_turtle.hideturtle()
# hossein_the_turtle.setheading(225)
# hossein_the_turtle.forward(300)
# hossein_the_turtle.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     hossein_the_turtle.dot(20, random.choice(color_list))
#     hossein_the_turtle.forward(50)
#
#     if dot_count % 10 == 0:
#         hossein_the_turtle.setheading(90)
#         hossein_the_turtle.forward(50)
#         hossein_the_turtle.setheading(180)
#         hossein_the_turtle.forward(500)
#         hossein_the_turtle.setheading(0)
#
#
#
# screen = Screen()
# screen.exitonclick()