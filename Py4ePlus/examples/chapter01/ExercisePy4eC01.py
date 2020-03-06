'''
Created on 06.03.2020

Hier werden die Aufgaben aus dem Kurs 'Python for everybody - Kapitel 1' gelöst.

@author: morrigan
@see: https://www.py4e.com/html3/01-intro
'''    
from examples import print_header
from examples import print_exercise 

print_header("Python for everybody - Kapitel 1 - Exercises")

# Exercise 1
question = "Exercise 1: What is the function of the secondary memory in a computer?"
code = ""
possible_answers = [
    "a) Execute all of the computation and logic of the program",
    "b) Retrieve web pages over the Internet",
    "c) Store information for the long term, even beyond a power cycle",
    "d) Take input from the user"
    ]
correct_answer = 2
print_exercise(question, code, possible_answers, correct_answer)

# Exercise 2
question = "Exercise 2: What is a program?"
code = ""
possible_answers = []
correct_answer = "A program is a series of stored instructions that a computer is able to execute sequentially, similar to a cooking recipe."
print_exercise(question, code, possible_answers, correct_answer)

# Exercise 3
question = "Exercise 3: What is the difference between a compiler and an interpreter?"
code = ""
possible_answers = []
correct_answer = "An interpreter reads the source code of the program as written by the programmer, parses the source code, and interprets the instructions on the fly.\n" \
                 "A compiler needs to be handed the entire program in a file, and then it runs a process to translate the high-level source code into machine language and then the compiler puts the resulting machine language into a file for later execution."
print_exercise(question, code, possible_answers, correct_answer)

# Exercise 4
question = "Exercise 4: Which of the following contains 'machine code'?"
code = ""
possible_answers = [
    "a) The Python interpreter",
    "b) The keyboard",
    "c) Python source file",
    "d) A word processing document"
    ]
correct_answer = 0
print_exercise(question, code, possible_answers, correct_answer)

# Exercise 5
question = "Exercise 4: Which of the following contains 'machine code'?"
code = """>>> primt 'hello world!'
File "<stdin>", line 1
  primt 'Hello world!'
                     ^
SyntaxError: invalid syntax
>>>"""
possible_answers = []
correct_answer = "'primt' is no correct key word. A correct statement is: print('Hello world!')"
print_exercise(question, code, possible_answers, correct_answer)

# Exercise 6
question = "Exercise 6: Where in the computer is a variable such as 'x' stored after the following Python line finishes?"
code = "x = 123"
possible_answers = [
    "a) Central processing unit",
    "b) Main Memory",
    "c) Secondary Memory",
    "d) Input Devices",
    "e) Output Devices"
    ]
correct_answer = 1
print_exercise(question, code, possible_answers, correct_answer)

# Exercise 7
question = "Exercise 7: What will the following program print out:"
code = """x = 43
x = x + 1
print(x)"""
possible_answers = [
    "a) 43",
    "b) 44",
    "c) x + 1",
    "d) Error because x = x + 1 is not possible mathematically"
    ]
correct_answer = 1
print_exercise(question, code, possible_answers, correct_answer)

# Exercise 8
question = "Exercise 8: Explain each of the following using an example of a human capability: (1) Central processing unit, (2) Main Memory, (3) Secondary Memory, (4) Input Device, and (5) Output Device. For example, 'What is the human equivalent to a Central Processing Unit'?"
code = ""
possible_answers = []
correct_answer = """(1) The human equivalent to the Central processing unit is the brain because it runs the "software" that you give it.
(2) Memory part of the brain because it goes away after someone dies.
(3) A book someone writes because it stays even after the person dies.
(4) The scenes such as ears to take input.
(5) The human voice, because it generates sounds that other people can understand."""
print_exercise(question, code, possible_answers, correct_answer)

# Exercise 9
question = "Exercise 9: How do you fix a 'Syntax Error'?"
code = ""
possible_answers = []
correct_answer = "Make sure that spelling is correct and ensure that all formating is correct, ex. do all quotation marks have the pair that they need."
print_exercise(question, code, possible_answers, correct_answer)











