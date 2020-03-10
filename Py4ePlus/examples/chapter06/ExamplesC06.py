'''
Created on 10.03.2020

In diesem Modul sind Beispiele zu folgenden Themen enthalten:
- Indizierung von Strings
- Slicing
- Bedingungen mit 'in'
- Wiederholungen

@author: morrigan
@see: https://www.py4e.com/html3/06-strings
@see: https://www.python-kurs.eu/python3_sequentielle_datentypen.php
'''
from examples import print_header

print_header("Kapitel 6 - Inidzierung von Strings")

strValue = "Hello world!"
print("'%s'.strValue[0] =" % strValue, strValue[0])
print("'%s'.strValue[len(strValue)-1] =" % strValue, strValue[len(strValue)-1])
print("'%s'.strValue[-1] =" % strValue, strValue[-1])
print("'%s'.strValue[-len(strValue)] =" % strValue, strValue[-len(strValue)])

print_header("Kapitel 6 - Slicing")

strValue = "Hello world!"
print("'%s'.strValue[1:5] =" % strValue, strValue[1:5])
print("'%s'.strValue[0:5] =" % strValue, strValue[0:5])
print("'%s'.strValue[:5] =" % strValue, strValue[:5])
print("'%s'.strValue[6:] =" % strValue, strValue[6:])
print("'%s'.strValue[:] =" % strValue, strValue[:])
strValue = "Python is very great!"
print("'%s'.strValue[2:15:3] =" % strValue, strValue[2:15:3])
print("'%s'.strValue[::4] =" % strValue, strValue[::4])

print_header("Kapitel 6 - Bedingungen mit 'in'")

strValue = "Hello world!"
print("'Hello' in '%s' =" % strValue, 'Hello' in strValue)
print("'World' in '%s' =" % strValue, 'World' in strValue)
print("'z' not in '%s' =" % strValue, 'z' not in strValue)

print_header("Kapitel 6 - Wiederholungen")

strValue = "+"
print("'%s' * 3 =" % strValue, strValue * 3)
# Vorsicht bei Referenzen!
x = ["a","b","c"]
y = [x] * 4
print("y =", y)
y[0][0] = "p"
print("y =", y)


