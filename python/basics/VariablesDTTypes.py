#Create variables for your name(string), age(integer), and GPA(float)
#Print each variable with a label (e.g., "Name: John").
# Change the value of the age variable and print it again.


# Assigning values to variables
# Type is not declared, python uses dynamic typing

name = "Katie"
age = 35
gpa = 4.5

age1 = age
# print the variable values with labels

print("Name :" , name)
print("Age :" , age)
print("Gpa :" , gpa)

# Memory address of age - before update

print("Address of Age  :", id(age))

print("Address of Age1 :", id(age1))


# print the type of variables

print("Type of Name :", type(name),"Type of Age:", type(age) , "Type of Gpa:", type(gpa))

# Assign new value to age and print it
age = 40

print("Updated Age:", age)

# Memory address of age

print("Address of Age :", id(age))