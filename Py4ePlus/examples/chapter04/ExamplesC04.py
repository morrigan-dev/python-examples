'''
Created on 06.03.2020

In diesem Modul sind Beispiele zu folgenden Themen enthalten
- Funktionen
- built-in Funktionen
- Konvertierung von Typen
- Mathematische Funktionen
- Eigene neue Funktionen

@author: morrigan
@see: https://www.py4e.com/html3/04-functions
@see: https://www.python-kurs.eu/python3_funktionen.php
'''
from examples import print_header

print_header("Kapitel 4 - Eigene Funktionen")


# Eigene neue Funktionen

# Funktion ohne Parameter
def sayHello():
    print("Hello")
sayHello()

# Funktion mit obligatorischen Argumenten
def say(welcomePhrase):
    print(welcomePhrase)   
say("Welcome")

# Funktion mit obligatorischen Argumenten und optionalen Parametern
def sayTo(welcomePhrase, name="everybody"):
    print(welcomePhrase, name)
sayTo("Hello")
sayTo("Hello", "Morrigan")

# Funktion mit einzeiligem DocString
def sayWithDocString(welcomePhrase):
    '''Gibt einen Willkommenstext auf der Konsole aus.'''
    print(welcomePhrase)
help(sayWithDocString)    

# Funktion mit mehrzeiligem DocString
def saySomethingWithString(welcomePhrase, name="everybody"):
    """Gibt einen Willkommenstext auf der Konssole aus
    
    Parameters:
    welcomePhrase (String): Ein Willkommenswort
    name (String): Optionale Angabe eines Namens - Default: everybody
    """
    print(welcomePhrase, name)
help(saySomethingWithString)

# Funktionsaufruf mit Schlüsselwortparameter
def sumsub(a, b, c=0, d=0):
    return a - b + c - d
print("sumsub(12, 4) ergibt:", sumsub(12, 4))
print("sumsub(12, 4, d=10) ergibt:", sumsub(12, 4, d=10))

# Funktion mit Rückgabeobjekt (Tuple) in dem mehrere Werte verpackt werden
def multipleResults(a, b, c):
    return (a*a, b*b, c*c)
print("multipleResults(1, 2, 3) ergibt:", multipleResults(1, 2, 3))

# Funktion mit beliebiger Anzahl an Parametern
def sumAll(*args):
    result = 0
    for x in args:
        result += x
    return result
print("sumAll() ergibt:", sumAll()) 
print("sumAll(1,2,3) ergibt:", sumAll(1,2,3))
print("sumAll(1,2,3,4,5,6,7,8,9) ergibt:", sumAll(1,2,3,4,5,6,7,8,9))


