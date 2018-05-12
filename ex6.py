#Chapter 6 Exercise

#declaring a variable
types_of_people = 10
#declaring a variable between the text
x = f"There are {types_of_people} types of people."
#declaring a string variable
binary = "binary"
do_not = "don't"

#declaring a string variable and used inside strings
y = f"Those who know {binary} and those who {do_not}."

#print varibales x and y
print(x)
print(y)

#print variables x and y with some text using curly braces as an inside string where 'f' used to format the string
print(f"I said: {x}")
print(f"I also said: {y}")

#declaring a boolean variable
hilarious = False

#declaring variable and constructing a string with a pair of curly braces as placeholder.
joke_evaluation = "Isn't that joke  so funny?! {}"

#using string formatter to concatinate varibale/string
print(joke_evaluation.format(hilarious))

#decaling string variables
w = "This is the left side of..."
e = "a string with a right side."

#print w and e variables together using '+' operator
print(w + e)

#Study Drill - Strings and Text

#1. Go through this program and write a comment above each line explaining it.
#See code above.

#2. Find all the places where a string is put inside a string. There are four places.
# At lines 6,12,19,20,26 there are strings which has been used inside the string and they are
# Six places in total.

#3. Are you sure there are only four places? How do you know? Maybe I like lying.
# In question 2 it was mentioned that there are four places where inside string were used, however
# at one end it's true but there are two strings also used in one line which makes a total of six. Please See
# line 12.

#4. Explain why adding the two strings w and e with + makes a longer string.
# A plus (+) operator basically concatinate or add the two variables together and make it a single long string.
