# LEARNING ABOUT LIST AND DICTIONARY COMPREHENSIONS

# # HERE WE ARE USING LIST COMPREHENSIONS AND CREATING A NEW SQUARES LIST IN A SINGLE LINE CODE
# num_list = [1,2,3,4,5]
# square_list = [num * num for num in num_list]
# print(square_list)

# # HERE WE ARE CREATING A NEW LIST ALL IN UPPERCASE ALPHABETS AND EVEN USING A CONDITION TO TEST
# name_list = ["vijay","durga","rao"]
# modified_list = [name.upper() for name in name_list if len(name) < 6]
# print(modified_list)

# # HERE WE ARE SPLITTING A STRING INTO SEPARATE ALPHABETS
# name = "vijay"
# list1 = [word.upper() for word in name]
# print(list1)

# # EXERCISE - 2, CREATE A NEW EVEN NUMBER LIST
# number = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [num for num in number if num % 2 == 0]
# print(result)

# from random import randint,seed
# # LEARNING ABOUT DICTIONARY COMPREHENSION
# seed(20)  #IT IS USED TO GENERATE SAME VALUES EACH TIME WE RUN IF NOT IT WILL DIFFERENT VALUES EACH TIME
# name_list = ["vijay","durga","rao","anjani","ravi","raja"]
# student_scores = {student:randint(1,100) for student in name_list}
# # print(student_scores)
# passing_students = {student:score for (student,score) in student_scores.items() if score >= 60}
# print(passing_students)

# sentence =  "what is the airspeed velocity of an unladen swallow?"
# separate_list = sentence.split()
# # print(separate_list)
# result = {word:len(word) for word in separate_list}
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }
# weather_f = {day:(temperature * 9/5) + 32 for (day,temperature) in weather_c.items()}
# print(weather_f)

# DICTIONARY COMPREHENSION BY USING PANDAS LIBRARY
# import pandas as p
# from random import randint,seed
# seed(20)  #IT IS USED TO GENERATE SAME VALUES EACH TIME WE RUN IF NOT IT WILL DIFFERENT VALUES EACH TIME
# name_list = ["vijay","durga","rao","anjani","ravi","raja"]
# student_scores = {student:randint(1,100) for student in name_list}
#
# dframe_students = p.DataFrame.from_dict(student_scores,orient='index',columns= ['score'])
# # print(dframe_students.index)
# print(dframe_students['score'].tolist())