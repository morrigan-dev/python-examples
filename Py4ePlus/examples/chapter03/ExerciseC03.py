'''
Created on 06.03.2020

Hier werden die Aufgaben aus dem Kurs 'Python for everybody - Kapitel 3' gelöst.

@author: morrigan
@see: https://www.py4e.com/html3/03-conditional
'''
from examples import print_header
from examples import print_exercise 

print_header("Python for everybody - Kapitel 3 - Exercises")

# Exercise 1
task = "Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours."
code = """Enter Hours: 45
Enter Rate: 10
Pay: 475.0"""
print_exercise(task, code, None, None)
strHours = input("Enter Hours: ")
strRate = input("Enter Rate: ")
if(strHours.isnumeric() and strRate.isnumeric()):
    hours = float(strHours)
    rate = float(strRate)
    pay = 0
    if(hours <= 40):
        pay = hours * rate
    else:
        hrsDiff = hours - 40
        additionalPay = hrsDiff * 1.5 * rate
        pay = 40 * rate + additionalPay    
    print("Pay:", round(pay, 2))
    print()

# Exercise 2
task = "Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:"
code = """Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input"""
print_exercise(task, code, None, None)
strHours = input("Enter Hours: ")
strRate = input("Enter Rate: ")
try:
    hours = float(strHours)
    rate = float(strRate)
    pay = 0
    if(hours <= 40):
        pay = hours * rate
    else:
        hrsDiff = hours - 40
        additionalPay = hrsDiff * 1.5 * rate
        pay = 40 * rate + additionalPay    
    print("Pay:", round(pay, 2))
    print()
except:
    print("Error, please enter numeric input")
    print()

# Exercise 3
task = "Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:"
code = """Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
 < 0.6     F
 
Enter score: 0.95
A

Enter score: perfect
Bad score

Enter score: 10.0
Bad score

Enter score: 0.75
C

Enter score: 0.5
F"""
print_exercise(task, code, None, None)
strScore = input("Enter score: ")
try:
    score = float(strScore)
    if(score > 1.0 or score < 0.0):
        print("Bad score")
    elif(score >= 0.9):
        print("A")
    elif(score >= 0.8):
        print("B")
    elif(score >= 0.7):
        print("C")
    elif(score >= 0.6):
        print("D")
    elif(score < 0.6):
        print("F")
except:
    print("Bad score")



