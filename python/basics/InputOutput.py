# Write a script that asks the user for their name and prints a greeting.
# Ask the user for their birth year and print their age.
# Use f-strings to display a formatted message using user input.

import datetime as d

v_name = input("Please enter your name:")

print("Welcome to python coding" , v_name)

v_year = int(input("Please enter your birth year:"))

v_current_year = d.datetime.now().year

v_age = v_current_year - v_year

print("Your current age is: ", v_age)

print(f"Welcome home! {v_name} , your present age is {v_age}")