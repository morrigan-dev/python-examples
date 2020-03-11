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

# Exercise 4
task = """Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt.  
Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of 
words using the split function. For each word, check to see if the word is already in a list. If the word is not in 
the list, add it to the list. When the program completes, sort and print the resulting words in alphabetical order."""
code = """Enter file: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']"""
print_exercise(task, code)
fname = input("Enter file name: ")
if(len(fname) < 1):
    fname = "romeo.txt"
fh = open(DATA_PATH / fname)
lst = list()
for line in fh:
    newWords = line.rstrip().split()
    for w in newWords:
        if(w not in lst):
            lst.append(w)

lst.sort()
print(lst)
print()

# Exercise 5
task = "Exercise 5: Write a program to read through the mail box data and when you find line that starts with 'From', \
you will split the line into words using the split function. We are interested in who sent the message, which is the \
second word on the From line."
code = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
print_exercise(task, code)
fname = input("Enter file name: ")
if(len(fname) < 1):
    fname = "mbox-short.txt"
fh = open(DATA_PATH / fname)
count = 0
for line in fh:
    if("From " not in line): continue
    email = line.split()[1]
    print(email)
    count += 1
print("There were", count, "lines in the file with From as the first word")
print()

# Exercise 6
task = "Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum \
and minimum of the numbers at the end when the user enters 'done'. Write the program to store the numbers the user \
enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop \
completes."
code = """Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0"""
print_exercise(task, code)
largest = None
smallest = None
while True:
    command = input("Enter a number: ")
    if(command == "done"): break

    num = 0    
    try:
        num = float(command)
    except:
        print("Invalid input")
        continue

    if(largest is None or largest < num):
        largest = num
    if(smallest is None or smallest > num):
        smallest = num    

print("Maximum is", largest)
print("Minimum is", smallest)
print()




