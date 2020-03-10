'''
Created on 10.03.2020

Hier werden die Aufgaben aus dem Kurs 'Python for everbody - Kapitel 7' gelöst.

@author: morrigan
@see: https://www.py4e.com/html3/08-lists
'''
from examples import print_header
from examples import DATA_PATH
from examples import print_exercise 

print_header("Python for everybody - Kapitel 8 - Exercises")

# Exercise 1
task = "Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, \
and returns None. Then write a function called middle that takes a list and returns a new list that contains all \
but the first and last elements."
print_exercise(task)

def chop(list_to_modify):
    del list_to_modify[0]
    del list_to_modify[len(list_to_modify)-1]

abc_list = ["A", "B", "C"]
print("abc_list (id, value) =", id(abc_list), abc_list)
chop(abc_list) 
print("abc_list (id, value) =", id(abc_list), abc_list)
print()

def middle(list_to_extract_middle):
    return list_to_extract_middle[1:len(list_to_extract_middle) - 1]

def_list = ["D", "E", "F"]
print("def_list (id, value) =", id(def_list), def_list)
def_list = middle(def_list)
print("def_list (id, value) =", id(def_list), def_list)
print()

# Exercise 2
task = "Exercise 2: Figure out which line of the above program is still not properly guarded. \
See if you can construct a text file which causes the program to fail and then modify the program \
so that the line is properly guarded and test it to make sure it handles your new text file."
code = """fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])"""
print_exercise(task, code)
fhand = open(DATA_PATH / "mbox-short2.txt")
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != "From" : continue
    # Hier könnte es sein, dass in der Datei eine Zeile mit 'From' beginnt, aber danach keine weiteren 
    # Wörter mehr kommen, sodass der Zugriff mit 'words[2]' zu einem Fehler führt.
    # Daher wird auch noch geprüft, ob es den Index=2 gibt
    if len(words) > 2: 
        print(words[2])
print()

# Exercise 3
task = "Exercise 3: Rewrite the guardian code in the above example without two if statements. \
Instead, use a compound logical expression using the or logical operator with a single if statement."
print_exercise(task)
fhand = open(DATA_PATH / "mbox-short2.txt")
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if(len(words) <= 2) or (words[0] != "From") : continue
    print(words[2])
print()


