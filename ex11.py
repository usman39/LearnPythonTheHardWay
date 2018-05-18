#Chapter 11 Exercise
print("What is you age?", end = '  ')
age = input()
print("what is your height?", end = '  ')
height = input()
print("What is your weight?", end = '  ')
weight = input()
print(f"You are {age} years old and you are {height} tall. Your weight is {weight}.")

#Study Drills

# 1. Go online and find out what Python’s input does.
#It allows the user to type something in, to input something.The value in
#input() always be a string.

# 2. Can you find other ways to use it? Try some of the samples you find.
# The other way "raw_input()" was used in Python 2 which is changed to input() in Python 3.
# -- IN PYTHON 2 --
# name = raw_input("Enter your name: ")
# print name
# -- IN PYTHON 3 --
# name = input("Enter your name: ")
# print (name)

# 3. Write another ”form” like this to ask some other questions.
print("How old are you?", end=' ')
age = int(input())
print("What is your height? e.g '6.7\' or '5.5\'=", end=' ')
height = float(input())
print("What is your weight?", end=' ')
weight = int(input())
print(f"According to the data you provided, you are {age} years old. Your height is {height}\nand your weight is {weight}.")
