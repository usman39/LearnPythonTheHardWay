#Chapter 5 Exercise

my_name = 'Zed A. Shaw'
my_age = 35 #not a lie
my_height = 71 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pound heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height  + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

#Study Drill - more variables and printing

#1. Change all the variables so there is no my_ in front of each one. Make sure you change the name
#everywhere, not just where you used = to set them.

name = "Zed A. Shaw"
age = 35 #not lie
height = 71 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pound heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

#2. Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do
# not just type in the measurements. Work out the math in Python.

name = "Zed A. Shaw"
age = 35 #not lie
height_cm = round(71 / 0.39370) #cm
weight_kg = round(180 * 0.45359237) #kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_cm} centimeter tall.")
print(f"He's {weight_kg} kilogram heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right

total = age + height_cm + weight_kg
print(f"If I add {age}, {height_cm}, and {weight_kg} I get {total}.")
