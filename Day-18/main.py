# from turtle import Turtle,Screen
# import random

# from PIL.ImageChops import screen


# def color_change():
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     color =(r,g,b)
#     return color

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.speed("fastest")
# #
# # # def tortise_drawings(value):
# # #     num_of_sides = value
# # #     initial_sides = 3
# # #     color_change()
# # #     while num_of_sides >= initial_sides:
# # #         angle = 360 - num_of_sides
# # #         for item in range(num_of_sides):
# # #             timmy.forward(40)
# # #             timmy.right(angle)
# # #          num_of_sides -= 1
# #
# #
# #
# #
# # # direction = [0,90,180,270]
# # #
# # #
# # for item in range(200):
# #     timmy.pensize(10)
# #     timmy.forward(40)
# #     timmy.right(random.choice(direction))
# #     color_change()

# # # -------------------spirograph------------------
# # #
# def spirograph(size_of_the_gap):
#     for _ in range(int(360/size_of_the_gap)):
#         timmy.color(color_change())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_the_gap)

# spirograph(5)
# my_screen = Screen()
# my_screen.exitonclick()
# #
# # # --------------------hirst painting------------------------------------------
# #
# # timmy.setheading(225)
# # timmy.penup()
# # timmy.hideturtle()
# # timmy.forward(250)
# # timmy.setheading(0)
# # timmy.pendown()
# # number_of_dots = 101
# # for dot_count in range(1,number_of_dots):
# #     timmy.dot(10,color_change())
# #     timmy.penup()
# #     timmy.forward(50)
# #     timmy.pendown()
# #     if dot_count % 10 ==0 :
# #         timmy.setheading(90)
# #         timmy.penup()
# #         timmy.forward(50)
# #         timmy.setheading(0)
# #         timmy.setheading(180)
# #         timmy.forward(500)
# #         timmy.setheading(0)
# #         timmy.pendown()
# # my_screen = Screen()
# # my_screen.exitonclick()