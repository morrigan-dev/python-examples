'''
Created on 06.03.2020

Hier werden die Aufgaben aus dem Kurs 'Python for everybody - Kapitel 2' gelöst.

@author: morrigan
@see: https://www.py4e.com/html3/02-variables
'''
from examples import print_header
from examples import print_exercise 

print_header("Python for everybody - Kapitel 2 - Exercises")

# Exercise 2
task = "Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them."
code = """Enter your name: Chuck
Hello Chuck"""
print_exercise(task, code, None, None)
name = input("Enter your name: ")
print("Hello", name)
print()

# Exercise 3
task = "Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay."
code = """Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25"""
print_exercise(task, code, None, None)
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
if(hours.isnumeric() and rate.isnumeric()):
    pay = float(hours) * float(rate)
    print("Pay:", round(pay, 2))

# Exercise 4
task = "Exercise 4: Assume that we execute the following assignment statements:"
code = """width = 17
height = 12.0

For each of the following expressions, write the value of the expression and the type (of the value of the expression).
    1. width//2
    2. width/2.0
    3. height/3
    4. 1 + 2 * 5"""
correct_answer = """1. int
2. float
3. float
4. int"""
print_exercise(task, code, None, correct_answer)
width = 17
height = 12.0
print("Type of 'width//2':", type(width//2))
print("Type of 'width/2.0':", type(width/2.0))
print("Type of 'height/3':", type(height/3))
print("Type of '1 + 2 * 5':", type(1 + 2 * 5))

# Exercise 5
task = "Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature."
print_exercise(task, None, None, None)
celsius = input("Enter a temperature in celsius: ")
fahrenheit = float(celsius) * 1.8 + 32
print("temperature in fahrenheit is", fahrenheit)





