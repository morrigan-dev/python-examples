'''
Created on 10.03.2020

Hier werden die Aufgaben aus dem Kurs 'Python for everbody - Kapitel 7' gelöst.

@author: morrigan
@see: https://www.py4e.com/html3/07-files
'''
from examples import print_header, DATA_PATH
from examples import print_exercise 

print_header("Python for everybody - Kapitel 7 - Exercises")

# Exercise 1
task = "Exercise 1: Write a program to read through a file and print the contents of the file (line by line) \
all in upper case. Executing the program will look as follows:"
code = """python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
     BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
     SAT, 05 JAN 2008 09:14:16 -0500"""
print_exercise(task, code)
filename = "mbox-short.txt"
print("Dateiinhalt von {} in Großbuchstaben:".format(filename))
try:
    with open(DATA_PATH / filename) as fileHandle:
        for line in fileHandle:
            print(line.upper())
except IOError as e:
    print("Die Datei '{}' konnte nicht geöffnet werden. Ursache: {}".format(filename, e.args[1]))
print()        

# Exercise 2
task = """Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines 
of the form:
X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with 'X-DSPAM-Confidence:' pull apart the line to extract the floating-point 
number on the line. Count these lines and then compute the total of the spam confidence values from these lines. 
When you reach the end of the file, print out the average spam confidence."""
code = """Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519"""
print_exercise(task, code)
filename = input("Enter a filename: ")
try:
    with open(DATA_PATH / filename) as file_handle:
        counter = 0
        total = 0
        for line in file_handle:
            if not line.startswith("X-DSPAM-Confidence:"): continue
            stripped_line = str(line).rstrip();
            number = float(stripped_line[stripped_line.find(":")+2:])
            total += number
            counter += 1
        print("Average spam confidence:", total / counter)
except IOError as e:
    print("Die Datei '{}' konnte nicht geöffnet werden. Ursache: {}".format(filename, e.args[1]))
print()

# Exercise 3
task = """Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless \
Easter Egg to their program. Modify the program that prompts the user for the file name so that it prints \
a funny message when the user types in the exact file name "na na boo boo". \
The program should behave normally for all other files which exist and don't exist. \
Here is a sample execution of the program:"""
code = """python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt

python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt

python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!"""
print_exercise(task, code)
filename = input("Enter the file name: ")
if(filename == "na na boo boo"):
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:    
    try:
        with open(DATA_PATH / filename) as file_handle:
            counter = 0
            for line in file_handle:
                if line.startswith("Subject:"):
                    counter += 1
            print("There were {} subject lines in {}".format(counter, filename))
    except IOError as e:
        print("File cannot be opened: {}".format(filename))
print()




