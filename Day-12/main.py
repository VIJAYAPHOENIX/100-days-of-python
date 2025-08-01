# # different types of scopes
# # local scope :- It is used to define a function or a operation.Which are already in a function or block. The function is only work within the function.
# # Global scope :- It is a variable declared globally. It can be used through-out the program

# number = 3 #it is a global variable
# def operator():
#     number = 2 #it is a local variable

# there is no block scope in python

# # Global scope variable is very hard to modify in a function . Because it can rise errors.But if you want to use a global variable in a local function.we use keyword "global"

# enemies = 1

# def game():
#     global enemies
#     enemies +=2
#     return enemies

# print(game())

# Global constants is all in capitals that there values never gonna change

# PI = 3.14 #Global constant

# project number guessing
# import random
# import clear
#
#
#
# def chosed_number():
#     number = random.randrange(1,101)
#     return number
#
# def game_start(choices,selected_number):
#     game_ends = False
#     guess = 0
#     while not game_ends:
#         print(f"you have {choices - guess} chances")
#         if choices > guess:
#             value = int(input("Enter your guessed number :- "))
#             if value > selected_number:
#                 print("Too High")
#             elif value < selected_number:
#                 print("Too low")
#             elif value == selected_number:
#                 game_ends = True
#                 print(f"You got it {selected_number} is correct")
#             guess += 1
#         elif choices == guess:
#             print(selected_number)
#             game_ends = True
#
# selected_number = 0
# print("Welcome to the Number Guessing Game")
# print("I'm thinking a number between 1 to 100.")
# pick = input("Choose a difficulty.Type 'easy' or 'hard' :- ")
# selected_number = chosed_number()
# if pick == "hard":
#     choices = 5
# elif pick == "easy":
#     choices = 10
# else:
#     print ("enter a valid option")
# game_start(choices,selected_number)
# print(selected_number)

# import random

# def chosed_number():
#     number = random.randrange(1, 101)
#     return number

# def game_start(choices, selected_number):
#     game_ends = False
#     guess = 0  # Track the number of guesses made
#     while not game_ends:
#         print(f"You have {choices - guess} chances left.")
#         if guess < choices:
#             value = int(input("Enter your guessed number: "))
#             if value > selected_number:
#                 print("Too High!")
#             elif value < selected_number:
#                 print("Too Low!")
#             elif value == selected_number:
#                 game_ends = True
#                 print(f"You got it! {selected_number} is correct.")
#             guess += 1
#         else:
#             game_ends = True
#             print("You've run out of guesses.")

# selected_number = chosed_number()
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")
# pick = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# if pick == "hard":
#     choices = 5
# elif pick == "easy":
#     choices = 10
# else:
#     print("Invalid option. Exiting the game.")
#     exit()

# game_start(choices, selected_number)
