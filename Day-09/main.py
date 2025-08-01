# # creating and learning about dictionaries
# first_dictionary = {
#     "bug":"some sort of error in the program",
#     "debug":"solving or rectifing the error",
#     "function":"a group of instructions"
# }
# # to edit a key value in a dictionary
# first_dictionary["function"] = "a set of instructions which are used to call anytime"
# # # to create a empty dictionary
# # empty_dic = {}
# # print(empty_dic)
# # # to empty a existing dictionary
# # first_dictionary = {}
# first_dictionary["loop"] = "repeat the code number of times"
# for key in first_dictionary:
#     print(key)
#     print(first_dictionary[key])

# # coding exercise grading program
# student_marks = {
#     "Aditya":81,
#     "Anurag":80,
#     "Bhanu":79,
#     "Durga Rao":85,
#     "Vijay":93
# }
# student_grades = {}
# for key in student_marks:
#     if student_marks[key] >= 91 and student_marks[key] <= 100:
#         student_grades[key] = "outstanding"
#     elif student_marks[key] >= 81:
#         student_grades[key] = "exceeds Expectations"
#     elif student_marks[key] >= 71:
#         student_grades[key] = "Above average"
#     else:
#         student_grades[key] = "Average"
    
# print(student_grades)

# # nesting dictionary in a dictionary
# travel = {
#     {
#         "location":"Tatipaka",
#         "visited_places":["school","college","theatre"],
#         "total_visits":2000
#     },
#     {
#         "location":"Amalapuram",
#         "visited_places":["college","bus_stop"],
#         "total_visits":300
#     }
# }

# # nesting dictionaries in a list
# travel = [
#     {
#         "location":"Tatipaka",
#         "visited_places":["school","college","theatre"],
#         "total_visits":2000
#     },
#     {
#         "location":"Amalapuram",
#         "visited_places":["college","bus_stop"],
#         "total_visits":300
#     }
# ]

# def add_to_list(location,visited_places,total_visits):
#     new_dic = {}
#     new_dic["location"] = location
#     new_dic["visited_places"] = visited_places
#     new_dic["total_visits"] = total_visits
#     travel.append(new_dic)

# add_to_list("Gannavaram",["classes","theatre"],1000)
# print(travel)

# mini project for day-9
from replit import clear

print("welcome to the secret auction ")

def find_winner(bids):
    highest_bid = 0
    winner = ""
    for bidders in bids:
        bidding_amount = bids[bidders]
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidders
    print(f"winner of this auction is {winner} with an amount of ${highest_bid}")


bids = {}
auction_ended = False
while not auction_ended:
    name = input("please enter your name :-\n").lower()
    bid = int(input("enter the bidding amount :-\n"))
    bids[name] = bid
    action = input("is there any other bidder? Type 'yes' or 'no' :-\n").lower()
    if action == "no":
        find_winner(bids)
        auction_ended = True
    elif action == "yes":
        clear()

