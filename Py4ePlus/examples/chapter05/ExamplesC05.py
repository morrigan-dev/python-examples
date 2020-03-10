'''
Created on 10.03.2020

In diesem Modul sind Beispiele zu folgenden Themen enthalten:
- for-Schleife
- while-Schleife


@author: morrigan
@see: https://www.py4e.com/html3/05-iterations
@see: https://www.python-kurs.eu/python3_schleifen.php
@see: https://www.python-kurs.eu/python3_for-schleife.php
'''
from examples import print_header

print_header("Kapitel 5 - for-Schleife")


# Zählen von 1 bis 10 mit einer for-Schleife und der range() Funktion
for i in range(1, 11):
    print(i)
print()    

# Gebe die 7er Reihe aus
base = 7
for i in range(base, 10*base + base, base):
    print(i)
print()    

# Berechnung von Pythagoräischen Zahlen
from math import sqrt
n = int(input("Maximale Zahl? "))
for a in range(1,n+1):
    for b in range(a,n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if ((c_square - c**2) == 0):
            print(a, b, c)
print()

# Summe von 1 bis 100 mit einer for-Schleife
n = 100
s = 0
for counter in range(1,n+1):
    s += counter
print("Sum of 1 until " + str(n) + ": " + str(s) )
print()

# Iteration durch Listen mit einer for-Schleife
languages = ["C", "C++", "Java", "Python"]
for language in languages:
    print(language)

# for-Schleife mit else-Block der am Ende der Schleife ausgeführt wird
items = ["A", "B", "C"]
for item in items:
    print(item)
else:
    print("Alle Items wurden ausgegeben")
print()

items = ["A", "B", "C"]
cancel_item = "B"
for item in items:
    print(item)
    if(item == cancel_item): break
else:
    print("Alle Items wurden ausgegeben")
print("Es wurde nach %s abgebrochen" % cancel_item)
print()

# Beispiel einer Listen-Iteration mit Seiteneffekten
colours = ["red"]
for i in colours:
    if i == "red":
        colours += ["black"]
    if i == "black":
        colours += ["white"]
print(colours)


print_header("Kapitel 5 - while-Schleife")


# Zählen von 1 bis 10
i = 1
while i<=10:
    print(i)
    i += 1
print()
    
# Eingabe mit sys ähnlich zu der input-Funktion
import sys
text = ""
print("Ihre Eingabe: ")
while True:
    c = sys.stdin.read(1)
    if(c == '\n'):
        break
    text = text + c
print("Sie haben '%s' eingegeben"  % text)
print()

# Beispiel für eine Nutzung des else Blocks in einer Schleife unter Nutzung eines Abbruches mit break
import random
n = 20
to_be_guessed = random.randint(1,n)

print("Ich habe mir eine Zahl zwischen 0 und 20 ausgedacht. Errate sie... oder gibt mit -1 auf")
guess = 0
while guess != to_be_guessed:
    guess = int(input("Neuer Versuch: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Zu gross")
        elif guess < to_be_guessed:
            print("Zu klein")
    else:
        print("Schade, dass du aufgibst!")
        break
else:
    print("Gratuliere, das war's")


