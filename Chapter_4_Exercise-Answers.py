#Chapter 4 Variables Exercise
#Using of variables in Python

#A variable is a name of anything like human have name. Programmers use good
#variable names which help them to read their code more easily.

#define number of cars
cars = 100
#define how much capacity is available that a car can carry passengers
space_in_cars = 4
#define number of drivers available
drivers = 30
#define number of passengers
passengers = 90
#calculate how many cars will not driven depending on number of drivers
cars_not_driven = cars - drivers
#calculate how many cars will be driven according to drivers availability
cars_driven = drivers
#calculate how many passengers in a carpool
carpool_capacity = cars_driven * space_in_cars
#calculate how many passengers can sit in each car?
average_passengers_per_car = passengers / cars_driven

print("There are ", cars , "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#Chapter 4 Variables - Study Drills

#0. Explain this error in your own words. Make sure you use line numbers and explain why.
#Traceback ( most recent call last ) :
#File ”ex4.py ” , line 8 , in <module>
#average_passengers_per_car = ca r _pool _capacity / passenger
#NameError : name ’ ca r _pool _capacity ’ is not defined

#In the above error the Python compiler pointing out that the error is at
#line 8 where the variable name "car_pool_capacity" is wrong and also "passenger"
#name is wrong. The declaration of these variables were carpool_capacity and
#passengers. Therefore, when the complier read at line 8 it couldn't recognized
#the variable names and triggered error.

# 1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it’s just 4?
#No Difference. I run the code even with "4" and I didn't found any
#difference in result. 4.0 is a floating point number. It's just a number with
#the decimal point. If float not use than it will not be permitted in the answer.

#2. Remember that 4.0 is a floating point number. It’s just a number with a decimal point, and you
# need 4.0 instead of just 4 so that it is floating point.

# Just memorised by your own.

#3. Write comments above each of the variable assignments.
# Please see at code above.

#4. Try running python3.6 from the Terminal as a calculator like you did before, and use variable
# names to do your calculations. Popular variable names are also i, x, and j.

i = 36
x = 45
j = i * x

print("The answer 36 * 45 is" , j  )
