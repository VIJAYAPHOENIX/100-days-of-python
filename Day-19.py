from turtle import Turtle,Screen
import random
my_screen = Screen()
colors =["red","orange","purple","blue","yellow","green"]
y_points = [-70,-40,-10,20,50,80]
is_race_on = False
user_bet = my_screen.textinput(title="place your bet",prompt="which turtle will win?? enter color: ")
all_turtles = []
my_screen.setup(width=500,height=400)

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_points[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"you win ,the {winning_turtle} turtle is the winner!")
            else:
                print(f"you lose ,the {winning_turtle} turtle is the winner!")
        rand_distances = random.randint(0,10)
        turtle.forward(rand_distances)



my_screen.listen()
my_screen.exitonclick()