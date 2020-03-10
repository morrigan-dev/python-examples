'''
Created on 06.03.2020

Hier werden die Aufgaben aus dem Kurs 'Python for everybody - Kapitel 4' gelöst.

@author: morrigan
@see: https://www.py4e.com/html3/04-functions
@see: https://www.python-kurs.eu/python3_funktionen.php
'''
from examples import print_header
from examples import print_exercise 
import random

print_header("Python for everybody - Kapitel 4 - Exercises")

# Exercise 1
question = "Exercise 1: Run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get."
print(question, None, None, None)
print("random.randint(5, 10):", random.randint(5, 10))
print("random.randint(5, 10):", random.randint(5, 10))
t = [1, 2, 3]
print("t = [1, 2, 3]")
print("random.choice(t):", random.choice(t))
print("random.choice(t):", random.choice(t))
print()

# Exercise 2
question = "Exercise 2: Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get."
# Nicht möglih, da es bereits zu Compilerfehlern kommt...
# Eine Funktion muss immer oberhalb des ersten Aufrufs definiert werden.

# Exercise 3
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


repeat_lyrics()
print()

# Exercise 4
question = "Exercise 4: What is the purpose of the 'def' keyword in Python?"
possible_answers = [
    "a) It is slang that means 'the following code is really cool'",
    "b) It indicates the start of a function",
    "c) It indicates that the following indented section of code is to be stored for later",
    "d) b and c are both true",
    "e) None of the above"
    ]
correct_answer = 1
print_exercise(question, None, possible_answers, correct_answer)

# Exercise 5
question = "Exercise 5: What will the following Python program print out?"
code = """def fred():
   print("Zap")

def jane():
   print("ABC")

jane()
fred()
jane()"""
possible_answers = [
    "a) Zap ABC jane fred jane",
    "b) Zap ABC Zap",
    "c) ABC Zap jane",
    "d) ABC Zap ABC",
    "e) Zap Zap Zap"
    ]
correct_answer = 3
print_exercise(question, code, possible_answers, correct_answer)

# Exercise 6
task = "Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate)."
code = """Enter Hours: 45
Enter Rate: 10
Pay: 475.0"""
print_exercise(task, code, None, None)

def computepay(hours, rate):
    pay = 0
    if(hours <= 40):
        pay = hours * rate
    else:
        hrsDiff = hours - 40
        additionalPay = hrsDiff * 1.5 * rate
        pay = 40 * rate + additionalPay
    return round(pay, 2)

strHours = input("Enter Hours: ")
strRate = input("Enter Rate: ")
if(strHours.isnumeric() and strRate.isnumeric()):
    print("Pay:", computepay(float(strHours), float(strRate)))
    print()

# Exercise 7
task = "Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string."
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

def computegrade(strScore):
    grade = None
    try:
        score = float(strScore)
        if(score > 1.0 or score < 0.0):
            grade = "Bad score"
        elif(score >= 0.9):
            grade = "A"
        elif(score >= 0.8):
            grade = "B"
        elif(score >= 0.7):
            grade = "C"
        elif(score >= 0.6):
            grade = "D"
        elif(score < 0.6):
            grade = "F"
    except:
        grade = "Bad score"
    return grade    

strScore = input("Enter score: ")
print(computegrade(strScore))

