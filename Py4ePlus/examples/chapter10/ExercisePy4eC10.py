'''
Created on 12.03.2020

Hier werden die Aufgaben aus dem Kurs 'Python for everbody - Kapitel 10' gelöst.

@author: morrigan
@see: https://www.py4e.com/html3/10-tuples
'''
import string

from examples import DATA_PATH
from examples import print_exercise
from examples import print_header

print_header("Python for everybody - Kapitel 10 - Exercises")

# Exercise 1
task = "Exercise 1: Revise a previous program as follows: Read and parse the 'From' lines and pull out the addresses \
from the line. Count the number of messages from each person using a dictionary. \
After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples \
from the dictionary. Then sort the list in reverse order and print out the person who has the most commits."
code = """Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195"""
print_exercise(task, code)
filenames = ["mbox-short.txt", "mbox.txt"]
for fname in filenames:
    counter_dict = dict()
    with open(DATA_PATH / fname) as file_handle:
        for line in file_handle:
            if line.startswith("From "):
                words = line.split()
                if len(words) >= 2:
                    address = words[1]
                    counter_dict[address] = counter_dict.get(address, 0) + 1
    # print("counter_dict =", counter_dict)
    counter_list = []
    for (address, amount) in counter_dict.items():
        counter_list.append((amount, address))
    # print("counter_list =", counter_list)
    counter_list.sort(reverse=True)
    print(counter_list[0][1], counter_list[0][0])

# Exercise 2
task = "Exercise 2: This program counts the distribution of the hour of the day for each of the messages. \
You can pull the hour from the 'From' line by finding the time string and then splitting that string into parts \
using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, \
sorted by hour as shown below."
code = """python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1"""
print_exercise(task, code)
counter_dict = dict()
with open(DATA_PATH / "mbox-short.txt") as file_handle:
    for line in file_handle:
        if line.startswith("From "):
            words = line.split()
            if len(words) >= 6:
                date = words[5]
                hour = date.split(":")[0]
                counter_dict[hour] = counter_dict.get(hour, 0) + 1
print("counter_dict =", counter_dict)
counter_list = list(counter_dict.items())
print("counter_list =", counter_list)
counter_list.sort()
for (hour, amount) in counter_list:
    print(hour, amount)

# Exercise 4:
task = "Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. \
Your program should convert all the input to lower case and only count the letters a-z. Your program should not \
count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different \
languages and see how letter frequency varies between languages. Compare your results with the tables at \
https://wikipedia.org/wiki/Letter_frequencies."
print_exercise(task)
counter_dict = dict()
total = 0
with open(DATA_PATH / "silmarillion.txt") as file_handle:
    for line in file_handle:
        line = line.translate(line.maketrans("", "", string.punctuation)).strip().lower()
        for letter in line:
            if "a" <= letter <= "z":
                counter_dict[letter] = counter_dict.get(letter, 0) + 1
                total += 1
counter_list = list(counter_dict.items())
counter_list.sort()
for (letter, amount) in counter_list:
    print(letter, amount * 100 / total)