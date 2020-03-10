'''
Created on 10.03.2020

Hier werden die Aufgaben aus dem Kurs 'Python for everbody - Kapitel 6' gelöst.

@author: morrigan
@see: https://www.py4e.com/html3/06-strings
@see: https://www.python-kurs.eu/python3_sequentielle_datentypen.php
@see: https://pyformat.info/
'''
from examples import print_header
from examples import print_exercise 

print_header("Python for everybody - Kapitel 6 - Exercises")

# Exercise 1
task = "Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards \
to the first character in the string, printing each letter on a separate line, except backwards."
print_exercise(task)
fruit = "banana"
index = len(fruit) - 1
while(index >= 0):
    print(fruit[index])
    index -= 1
print()

#Exercise 2
question = "Exercise 2: Given that fruit is a string, what does fruit[:] mean?"
correct_answer = "fruit[:] create a copy of the string fruit"
print_exercise(question, None, None, correct_answer)
fruit = "banana"
copyOfFruit = fruit[:]
print("fruit:", fruit)
print("copyOfFruit:", copyOfFruit)
print()

# Exercise 3
task = "Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string \
and the letter as arguments."
code = """
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)"""
print_exercise(task, code)

def count(word, letter):
    count = 0
    for letterOfWord in word:
        if letterOfWord == letter:
            count = count + 1
    return count
print("count('banana', 'a') =", count("banana", "a"))
print()

# Exercise 4
task = """Exercise 4: There is a string method called count that is similar to the function in the previous exercise.
Read the documentation of this method at:

https://docs.python.org/library/stdtypes.html#string-methods

Write an invocation that counts the number of times the letter a occurs in 'banana'."""
fruit = "banana"
print("fruit.count('a') =",fruit.count("a"))
print()

# Exercise 5
task = """Exercise 5: Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the colon character \
and then use the float function to convert the extracted string into a floating point number."""
print_exercise(task)
strValue = "X-DSPAM-Confidence:0.8475"
index = strValue.find(":")
number = float(strValue[index+1:])
print("Parsed number:", number)
print()

# Exercise 6
task = """Exercise 6: Read the documentation of the string methods at 
https://docs.python.org/library/stdtypes.html#string-methods
You might want to experiment with some of them to make sure you understand how they work. 
strip and replace are particularly useful.

The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), 
the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, 
then end is optional."""
strValue = "heLLo worLd"
print("'%s'.capitalize() =" % strValue, strValue.capitalize())
print("'%s'.casefold() =" % strValue, strValue.casefold())
print("'%s'.strValue.center(len(strValue) + 6, '+') =" % strValue, strValue.center(len(strValue) + 6, '+'))
print("'%s'.strValue.endswith('world') =" % strValue, strValue.endswith("worLd"))
print("'Hello {}!'.format('Morrigan') =", "Hello {}!".format("Morrigan"))







