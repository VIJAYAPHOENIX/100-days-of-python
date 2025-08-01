# import csv
#
# with open("./weather_data.csv") as data_file:
#
#     data = csv.reader(data_file)
#     temperature = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#         print(temperature)
# import turtle
# ABOUT PANDAS LIBRARY AND ITS FEATURES

# import pandas as p
#
# data = p.read_csv("weather_data.csv")

# print(type(data["temp"]))

# # CONVERTING "TEMP" INTO A LIST
# temp_list = data["temp"].to_list()
# print(temp_list)

# # CONVERTING CSV FILE DATA INTO DICTIONARY
# dict_data = data.to_dict()
# print(dict_data)

# # TO CALCULATE AVERAGE,MIN,MAX
# print(data["temp"].mean())
# print(data["temp"].min())
# print(data["temp"].max())

# # TO FIND A SPECIFIC RECORD ACCORDING TO THE CONDITION
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
# if we want specific attribute in a single record , we have to declare it separately.

# # TO CREATE A DATAFRAME FROM BEGINNING.
# data_dict = {
#     "name" : ["vijay","durga","rao"],
#     "score" : [98,91,90]
# }
#
# dataframe = p.DataFrame(data_dict)
# print(dataframe)
#
# # if we want to save this dataframe into a csv file
# dataframe.to_csv("just_demo_file.csv")

# import pandas as p
#
# data_file = p.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrel_count = 0
# red_squirrel_count = 0
# black_squirrel_count = 0
# for color in data_file["Primary Fur Color"]:
#     if color == "Gray":
#         grey_squirrel_count += 1
#     elif color == "Cinnamon":
#         red_squirrel_count += 1
#     elif color == "Black":
#         black_squirrel_count += 1
#
# data_dict = {"Color":["Gray","Cinnamon","Black"],
#              "Count":[grey_squirrel_count,red_squirrel_count,black_squirrel_count]}
#
# df = p.DataFrame(data_dict)
#
# df.to_csv("Squirrel_Count")

from turtle import Turtle,Screen
import pandas as p

data_file = p.read_csv("50_states.csv")

screen = Screen()
turtle = Turtle()
screen.title("BRAIN QUIZ")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = data_file.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    response = screen.textinput(title=f"{len(guessed_states)}/50 correct states",prompt="Enter name of the state").title()
    if response == "Exit":

    #     remaining_states = []
    #     for state in states:
    #         if state not in guessed_states:
    #             remaining_states.append(state)

        remaining_states = [name for name in states if name not in guessed_states]
        print(remaining_states)
        exit()
    elif response in states:
        guessed_states.append(response)
        t = Turtle()
        t.hideturtle()
        t.penup()
        selected_state = data_file[data_file.state == response]
        t.goto(int(selected_state.x),int(selected_state.y))
        t.write(response)
screen.exitonclick()