'''
Created on 05.03.2020

In diesem Modul sind Beispiele zu folgenden Themen enthalten
- Bedingte Anweisung
- Bedingte Anweisung mit Alternative
- Bedingte Anweisung mit mehreren Bedingungen
- Verschachtelte bedingte Anweisung
- Fehlerbehandlung
- Logische Ausdrücke

@author: morrigan
@see: https://www.py4e.com/html3/03-conditional
@see: https://www.python-kurs.eu/python3_bedingte_anweisungen.php
'''
from examples import print_header

print_header("Kapitel 3 - Bedingte Anweisungen")

# Einfache Bedingung
x = 5
if x > 0:
    print("x ist positiv")
    
# Verknüpfung mehrerer Bedingungen
if(x > 0 and x < 10):
    print("x ist positiv und einstellig")    
    
# Bedingung mit Alternative
if x % 2 == 0:
    print("x ist gerade")
else:
    print("x ist ungerade")    

# Bedingung mit mehreren Fällen
x = 10
y = 5
if x < y:
    print("x ist kleiner als y")
elif x > y:
    print("x ist größer als y")
else:
    print("x ist gleich y")

# Verschachtelte bedingte Anweisungen
if x == y:
    print("x ist gleich y")
else:
    if x < y:
        print("x ist kleiner als y")
    else:
        print("x ist größer als y")
        

print_header("Kapitel 3 - Fehlerbehandlung")

try:
    strValue = input("Geben Sie eine Ganzzahl ein: ")
    intValue = int(strValue)
    print("Ihre gewählte Ganzzahl ist:", str(intValue))
except:
    print("Sie haben keine Ganzzahl eingegeben!")
finally:
    print("Dieser Teil wird bei einem try-except Block immer ausgeführt.")
print()

def error_handling():
    while True:
        print("Vor dem Try Block")
        try:
            print("Innerhalb des try Blocks")
            input_value = input("Eingabe: ")
            if not input_value:
                break
            if input_value == "return":
                return
            x = int(input_value)
            print("Ihre Zahl ist:", x)

        except ValueError as e:
            print("Es ist ein Fehler aufgetreten: args={}, type={}".format(e.args[0], type(e)))
        else:
            print("Else Block")
        finally:
            print("Finally Block")
        print("Nach dem Try Block")
        print()

error_handling()
print()

try:
    raise ValueError("Fehler!")
except ValueError as e:
    print(e.args)


print_header("Kapitel 3 - Logische Ausdrücke")

print("a     | b     | not a | not b | a and b | a or b | a xor b")
a = False
b = False
print(a, "|", b, "|", not a, " |", not b," |", a and b, "  |", a or b, " |", a ^ b)
a = False
b = True
print(a, "|", b, " |", not a, " |", not b,"|", a and b, "  |", a or b, "  |", a ^ b)
a = True
b = False
print(a, " |", b, "|", not a, "|", not b," |", a and b, "  |", a or b, "  |", a ^ b)
a = True
b = True
print(a, " |", b, " |", not a, "|", not b,"|", a and b, "   |", a or b, "  |", a ^ b)





