'''
Created on 09.03.2020

Hier werden die Aufgaben aus dem Kurs 'Python for everbody - Kapitel 5' gelöst.

@author: morrigan
@see: https://www.py4e.com/html3/05-iterations
@see: https://www.python-kurs.eu/python3_schleifen.php
@see: https://www.python-kurs.eu/python3_for-schleife.php
'''
from examples import print_header
from examples import print_exercise 

print_header("Python for everybody - Kapitel 5 - Exercises")

# Exercise 1
question = "Exercise 1: Write a program which repeatedly reads numbers until the user enters 'done'. \
Once 'done' is entered, print out the total, count, and average of the numbers. \
If the user enters anything other than a number, detect their mistake using try and except \
and print an error message and skip to the next number."
code = """Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333"""
print_exercise(question, code)
count = 0
sumVal = 0
while(True):
    command = input("Enter a number: ")
    if(command == "done" or command == ""):
        break
    try:
        sumVal += int(command)
        count += 1
    except:
        print("Invalid input")
if(count > 0):
    print(sumVal, count, sumVal/count)
print()

# Exercise 2
question = "Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out \
both the maximum and minimum of the numbers instead of the average."
print_exercise(question)
minimum = None
maximum = None
while(True):
    command = input("Enter a number: ")
    if(command == "done" or command == ""):
        break
    try:
        number = int(command)
        if(minimum is None or number < minimum):
            minimum = number
        if(maximum is None or number > maximum):
            maximum = number   
    except:
        print("Invalid input")
print(minimum, maximum)
print()








