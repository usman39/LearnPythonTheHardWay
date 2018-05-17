#Chapter 10 Exercise

print("I am 6'2\" tall.")
print('I am 6\'2" tall.')
print("I 'understand\' Joe")

tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#Self Practice
first_cat = "\t I'm tabbed in."
second_cat = "I'm split\non a line."
third_cat = "I'm \\ a \\ cat."
fatty_cat = """
I'll do a list\n
\t* cat food
\t* Fishies
\t* catnip\n \t* Grass"""

print(first_cat)
print(second_cat)
print(third_cat)
print(fatty_cat)


#Chapter 10 study drills
# 1. Memorize all the escape sequences by putting them on flash cards.
# Created flashcards and memorised.
# 2. Use ''' (triple-single-quote) instead. Can you see why you might use that instead of """?
# It's all depend on the style and there is no difference either use """ or '''

# 3. Combine escape sequences and format strings to create a more complex format.

first_paragraph = """
\t Every human activity which is \n engaged in for the sake of earn \b profit \n is called business."""
some_math = round(43.5 + 89 / 22 * 10)
print(first_paragraph)
print("The answer for 43.5 + 89 / 22 * 10 \n \t ANSWER = ", some_math)
print("This computer have digital beep like \a ")
family = """They are four brothers and two sisters: \n here are the names: \n
\t* Jhon
\t* Mike
\t* Sean
\t* Steve
\t* Sarah
\t* Amber"""
print(family)
print("The length of this door is 10'11\" and other doors are 11'13\" ")
print("Hey, Aren't you 'Richard\', one who called last night?")
print('Exactly, "Mr Firgosan\", I\'m Richard, and I did called you last night.')
print("Look at these symbols: \n \t* \f known as 'Formfeed\' \n \t* \v known as 'Vertical tab\' ")
