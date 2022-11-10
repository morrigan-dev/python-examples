'''
Created on 10.03.2020

Hier werden die Aufgaben aus dem Kurs 'Python for everbody - Kapitel 9' gelöst.

@author: morrigan
@see: https://www.py4e.com/html3/09-dictionaries
'''
from examples import print_header
from examples import DATA_PATH
from examples import print_exercise

print_header("Python for everybody - Kapitel 9 - Exercises")

# Exercise 1
task = """Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn't matter what 
the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary."""
print_exercise(task)
with open(DATA_PATH / "words.txt") as file_handle:
    word_dict = dict()
    for line in file_handle:
        words = line.split()
        for word in words:
            word_dict[word] = True
    print("word_dict = {}".format(word_dict))
    print("'computer' in word_dict = {}".format("computer" in word_dict))
    print("'Alexa' in word_dict = {}".format("Alexa" in word_dict))
print()

# Exercise 2
task = """Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done.
To do this look for lines that start with "From", then look for the third word and keep a running count of each of 
the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

Sample Line:

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Sample Execution:"""
code = """python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}"""
print_exercise(task, code)
with open(DATA_PATH / "mbox-short.txt") as file_handle:
    counter_dict = dict()
    for line in file_handle:
        if line.startswith("From"):
            splitted_line = line.split()
            if len(splitted_line) > 2:
                day_of_week = splitted_line[2]
                counter_dict[day_of_week] = counter_dict.get(day_of_week, 0) + 1
print(counter_dict)
print()

# Exercise 3
task = "Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count \
how many messages have come from each email address, and print the dictionary."
code = """Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}"""
print_exercise(task, code)
with open(DATA_PATH / "mbox-short.txt") as file_handle:
    email_counter_dict = dict()
    for line in file_handle:
        if line.startswith("From: "):
            splitted_line = line.split()
            if len(splitted_line) > 1:
                email = splitted_line[1]
                email_counter_dict[email] = email_counter_dict.get(email, 0) + 1
print(email_counter_dict)
print()

# Exercise 4
task = "Exercise 4: Add code to the above program to figure out who has the most messages in the file. \
After all the data has been read and the dictionary has been created, look through the dictionary using \
a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print \
how many messages the person has."
code = """Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195"""
print_exercise(task, code)
email_counter_dict = dict()
with open(DATA_PATH / "mbox-short.txt") as file_handle:
    for line in file_handle:
        if line.startswith("From: "):
            splitted_line = line.split()
            if len(splitted_line) > 1:
                email = splitted_line[1]
                email_counter_dict[email] = email_counter_dict.get(email, 0) + 1
max_email_amount = 0
max_email = None
for (email, amount) in email_counter_dict.items():
    if amount > max_email_amount:
        max_email_amount = amount
        max_email = email
print(max_email, max_email_amount)

email_counter_dict = dict()
with open(DATA_PATH / "mbox.txt") as file_handle:
    for line in file_handle:
        if line.startswith("From: "):
            splitted_line = line.split()
            if len(splitted_line) > 1:
                email = splitted_line[1]
                email_counter_dict[email] = email_counter_dict.get(email, 0) + 1
max_email_amount = 0
max_email = None
for (email, amount) in email_counter_dict.items():
    if amount > max_email_amount:
        max_email_amount = amount
        max_email = email
print(max_email, max_email_amount)

# Exercise 5
task = "Exercise 5: This program records the domain name (instead of the address) where the message was sent from \
instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents \
of your dictionary."
code = """python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}"""
print_exercise(task, code)
with open(DATA_PATH / "mbox-short.txt") as file_handle:
    domain_counter_dict = dict()
    for line in file_handle:
        if line.startswith("From: "):
            splitted_line = line.split()
            if len(splitted_line) > 1:
                email = splitted_line[1]
                domain = email.split("@")[1]
                domain_counter_dict[domain] = domain_counter_dict.get(domain, 0) + 1
print(domain_counter_dict)
print()