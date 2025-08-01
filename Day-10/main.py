# # function with outputs

# def format_name(f_name,l_name):
#     formatted_fname = f_name.title()
#     formatted_lname = l_name.title()
#     return f"{formatted_fname} {formatted_lname}"

# print(format_name("vijay","grandhi"))

# # multiple return values

# def format_name(f_name,l_name):
#     if f_name == "" or l_name == "" :
#         return ("enter a valid input")
#     formatted_fname = f_name.title()
#     formatted_lname = l_name.title()
#     return f"{formatted_fname} {formatted_lname}"

# print(format_name(input("enter your first name :- \n"),input("enter your last name :-\n")))

# # mini project days of the month

# def is_leap(year):
#     if year % 4 == 0 :
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(year,month):
#     month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if is_leap(year)  and month == 2:
#         return 29
#     return month_days[month-1]

# year = int(input("enter the desired year :- \n"))
# month = int(input("enter the month :-\n"))
# days = days_in_month(year,month)
# print(days)

# # Docstring or pop-up message used describe about a funtion input and output types
# def format_name(f_name,l_name):
#     """enter your first and last name"""  #this is the docstring
#     formatted_fname = f_name.title()
#     formatted_lname = l_name.title()
#     return f"{formatted_fname} {formatted_lname}"

# print(format_name("vijay","grandhi"))

# calculator
from replit import clear
def add (n1,n2):
    return n1+n2

def subt(n1,n2):
    return n1-n2

def multiply (n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subt,
    "*": multiply,
    "/": divide
}
def calculator():
    end_point = True
    num1 = float(input("enter the first number :- "))
    for symbol in operations:
        print(symbol)
    while end_point :
        operant = input("choose a operation from the above operations :- ")
        num2 = float(input("enter the next number :- "))
        operation_function = operations[operant]
        result = operation_function(num1,num2)
        print(f"{num1} {operant} {num2} = {result}")
        repeat = input("if you want to operate on the previous result .Type 'yes'\n for new calculation .Type 'no' :- ")
        if repeat == "yes":
            num1 = result    
        elif repeat =="no":
            end_point = False
            clear()
            calculator()
        else:
            print("enter a valid input :-) ")

calculator()



