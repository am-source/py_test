# comment: str+k then str+c ||| uncomment str+k then str+u

# user_in = input()
# checkk = False
# name = "fu" + ("*" * 5)
# if type(user_in) == str:
#     checkk = True
# else:
#     checkk = False
# try:
#     numm = 5 - int(user_in)
#     print(numm)
# except:
#     print(f"False {name} \"input\"")

#########################
# from random import randint
# exit_vars = True
# print("Guess a number between 0 and 9!")
# while exit_vars:
#     print("Your guess is: ")
#     secret_num = randint(0, 9)
#     inputt = int(input())
#     if inputt == secret_num:
#         exit_vars = False
#         print("Correct!")
#     else:
#         print(f"Wrong guess! It was {secret_num}")

# str1 = "start"
# str2 = "stop"
# str3 = "quit"
# command = ""
# while True:
#     command = input().lower()
#     if command == str1:
#         print("Car Started... Ready to go!")
#     elif command == str2:
#         print("Car stopped.")
#     elif command == "help":
#         print('''start - to start the car
# stop - to stop the car
# quit - to exit''')
#     elif command == "quit":
#         break
#     else:
#         print("I don't understand your gibberish...")

# loops
# def simple_loopi(num):
#     for x in num:
#         print("*" * x)


# numvers = [5, 2, 5, 2, 2]
# simple_loopi(numvers)

# find largest num in list
# def findLargNum(listt):
#     if not listt:
#         return "Error"
#     tmpVar = listt[0]
#     for x in listt:
#         if x >= tmpVar:
#             tmpVar = x
#     return tmpVar

# CHECK NULL LIST:  if not list    (null list will be counted as false)

# print(findLargNum([]))

##
# numbers = [2, 7, 4, 9, 11, 6]
# print(11 in numbers)
# print(numbers.index(2))  # throws value-error if not in list

# numbers.sort()
# numbers2 = numbers.copy()

# use COPY() to copy sth instead of arg2 = arg1 if you dont want intact reference

# print(numbers == numbers2)
# numbers.reverse()
# print(numbers == numbers2)


# def removeDup(listt):
#     if not listt:
#         return "Error - Empty list!"
#     tmp = []
#     for item in listt:
#         if item in tmp:
#             continue
#         tmp.append(item)
#     return tmp


# print(removeDup([]))
# print(removeDup([1, 3, 4, 1, 5, 5, 7, 4, 4, 3]))

# tuples    TUPLES are IMMUTABLE
# numbers = (1,2,3)
# print(numbers[0])

# UNPACKING   tuples or list
# coordinates = (1,2,3)
# x,y,z = coordinates

# Dictionaries
# customer = {
#     "name": "Joe Schmo",
#     "age": 30,
#     "is_alive": True
# }
# can use customer["name"] but will throw if non existant,
# print(customer.get("name"))
# .get("name","abcd") would give abcd as default if name is non existant

# numberrs = {
#     0: "zero",
#     1: "one",
#     2: "two",
# }

# print("Put number here: ")
# i_user = input()
# outp = ""
# for x in i_user:
#     outp += numberrs.get(int(x)) + " "
# print(outp)

# STRING SPLIT
# mssg = "Hello Random 841"
# split_mssg = mssg.split(" ")

# CLASSES   use __init__ as constructor, __str__ for format in case like print()
# class Point:
#     x_val = ""
#     y_val = ""

#     def __init__(self, x, y):
#         self.x_val = x
#         self.y_val = y

#     def move(self, new_x, new_y):
#         self.x_val += new_x
#         self.y_val += new_y
#         return self

#     def __str__(self):
#         return f"({self.x_val}, {self.y_val})"

#     # def calc_dist(pos1,pos2):


# posA = Point(1, 5)
# print(posA)
# print(posA.move(10, 3))

# inheritance    use () after child class to list superior class
# class Mammal:
#     def walk(self):
#         print("walk")


# class Dog(Mammal):
#     def bite(self):
#         print("dog bites")

# class Cat(Mammal):
#     pass            ## pass used when lines expected but empty, emptiness ignored

# malmut = Dog()
# malmut.walk()


# importing:::     either import "module"  or   from "module" import "function"
# shortcut  e.g   import random as r  ......    r.randint()
# from random import randint    ....    randint()   even shorter

# import datetime
#
# noww = datetime.datetime.now()
# monthh = noww.strftime("%y")
# print(monthh)
#
# nowwww= "2021-10-05"
# nowwww_datetime = datetime.datetime.fromisoformat(nowwww)
# print(nowwww_datetime)
#
# for x in range(3):
#     print(x)
#---------------
# defining types in arg/pararm use sth like this
from typing import List


def list_fun(self, my_list:List):
    my_list.append("")
