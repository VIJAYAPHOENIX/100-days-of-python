# Defining functions
# def calliing():
#     print("hello haii somebody is calling you from there")

# calliing()
# def greet(name,location):
#     print(f"hai {name}")
#     print(f"your are from {location}")
#     print("am i right?")

# name = input("enter your name :- ").upper()
# location = input("where are you from :- ")
# # here name & locatin is called as position arguments
# greet(name,location)
# # from the below arguements are called as key arguements
# greet(name="vijay",location="gannavaram")

# # writing code logic to calculate paint area calculator
# # here we use math library to roundup the number
# import math
# def paint(height,length):
#   paint_coverage_per_can = 5
#   coverage =math.ceil((height*length)/paint_coverage_per_can)
#   print(f"Number of cans is needed is {coverage}")

# height = int(input("height of the wall :- "))
# length = int(input("length of the wall :- "))
# paint(height,length)

# def prime_check(number):
#     prime = False
#     for i in range(2,number-1):
#         if number == 0:
#             print("'0' is not a prime number")
#         elif number%i == 0:
#             print(f"number {number} is not a prime")
#         else:
#             prime = True
#     if prime :
#         print(f"number {number} is a prime")

# number = int(input("enter a number :- "))
# prime_check(number)
def coding(command):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if command == "encode":
        message = input("enter message to encode :-\n")
    elif command == "decode":
        message = input("enter message to decode :-\n")
    else:
        print("Enter a valid command")
    print(message)
    
command = input("type 'encode' to encrpt, type 'decode' to decrypt \n").lower()
coding(command)
