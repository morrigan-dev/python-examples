'''
Created on 12.03.2020

Hier werden die Aufgaben aus dem Kurs 'Python for everbody - Kapitel 11' gelöst.

@author: morrigan
@see: https://www.py4e.com/html3/11-regex
'''
import re
from examples import DATA_PATH
from examples import print_exercise
from examples import print_header

print_header("Python for everybody - Kapitel 11 - Exercises")

# Exercise 1
task = "Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user \
to enter a regular expression and count the number of lines that matched the regular expression:"
code = """$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4175 lines that matched java$"""
print_exercise(task, code)
filename = "mbox.txt"
input = input("Enter a regular expression: ")
if len(input) < 1:
    regex_list = ["^Author", "^X-", "java$"]
else:
    regex_list = [input]
for regex in regex_list:
    matching_lines = 0
    with open(DATA_PATH / filename) as file_handle:
        for line in file_handle:
            if re.search(regex, line):
                matching_lines += 1
    print("{} had {} lines that matched {}".format(filename, matching_lines, regex))


# Exercise 2
task = """Exercise 2: Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression and the findall() method. 
Compute the average of the numbers and print out the average as an integer."""
code = """Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756"""
print_exercise(task, code)
filenames = ["mbox.txt", "mbox-short.txt"]
for filename in filenames:
    value_list = []
    with open(DATA_PATH / filename) as file_handle:
        for line in file_handle:
            matching_values = re.findall("New Revision: ([0-9]*)", line)
            if len(matching_values) > 0:
                value_list.extend(matching_values)
    total = len(value_list)
    sum_value = 0
    for value in value_list:
        sum_value += int(value)
    print("{} -> {}".format(filename, int(sum_value / total)))
