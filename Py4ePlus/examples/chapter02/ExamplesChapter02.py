'''
Created on 04.03.2020

In diesem Modul sind Beispiele zu folgenden Themen enthalten
- Variablen
- Datentypen
- Zuweisung
- Ausdrücke
- Operationen

@author: morrigan
@see: https://www.py4e.com/html3/02-variables
@see: https://www.python-kurs.eu/python3_variablen.php
@see: https://www.python-kurs.eu/python3_operatoren.php
'''
from random import SystemRandom

print()
print("Kapitel 2 - Beispiele zu Variablen")
print("==================================")
print()

# Nummerische Datentypen
# - int        Ganzzahlen
# - float      Gleitkommazahlen
# - complex    Komplexe Zahlen
# - bool       Wahrheitswerte
intValue = 42  # normaler Integer
octalValue = 0o11  # octaler Integer
hexValue = 0x1A  # hexadezimaler Integer
binValue = 0b101010  # binärer Integer
floatValue = 42.0
complexValue = 42j
boolValue = True

# Ausgabe der Typinformation der einzelnen Variablen
print("Datentyp von intValue:", type(intValue), "->", intValue)
print("Datentyp von octalValue:", type(octalValue), "->", oct(octalValue))
print("Datentyp von hexValue:", type(hexValue), "->", hex(hexValue))
print("Datentyp von binValue:", type(binValue), "->", bin(binValue))
print("Datentyp von floatValue:", type(floatValue))
print("Datentyp von complexValue:", type(complexValue))
print("Datentyp von boolValue:", type(boolValue))

# Eine einfache Zuweisung eines Wertes zu einer Variablen
x = 42
print("Einfache Zuweisung:", x)

# Ein einfacher Ausdruck (Term auf de rechten Seite des Gleichheitszeichens
# und anschließender Zuweisung.
x = x + 1
print("Ergebnis nach Addition von 1:", x)
# Erweiterte Zuweisung der obigen Zeile (ein x++ wie z.B. in Java gibt es nicht)
# Achtung! Es gibt Implementierungsunterschiede bei den beiden Schreibweisen, später mehr dazu...
x += 1
print("Ergebnis nach Addition von 1 in erweiterter Zuweisung:", x)

# Ein Datentyp einer Variablen kann sich zur Laufzeit ändern
print("Datentyp von x vorher:", type(x), "Wert:", x)
x = x - 1.58
print("Datentyp von x nachher:", type(x), "Wert:", x)

# Variablen sind in Python grundsätzlich Objekte und referenzieren daher immer auf beliebige Objekte
x = 42
print("Identität von x:", id(x))
y = x
print("Identität von x und y:", id(x), id(y))
y = 78
print("Identität von x und y:", id(x), id(y))

# Gültige Variablennamen
# Python unterstützt Unicode, sodass der komplette Unicode Zeichensatz verwendet werden könnte.
# Davon ist jedoch abzuraten, um Probleme mit anderen Programmen, die z.B. den Quellcode anzeigen 
# oder analysieren, zu vermeiden.
height = 10
maximum_height = 100
MinimumHeight = 1
random0to1 = SystemRandom.random(SystemRandom)

# Ganzzahlige Division
x = 10 / 3
print("10 / 3 =", x, type(x))
x = 10 / 2
print("10 / 2 =", x, type(x))

# Division mit Abschneiden
x = 10 // 3
print("10 // 3 =", x, type(x))
x = 10 // 2
print("10 // 2 =", x, type(x))

# Datentyp: String
strValue = "Python"
print(strValue)

# Strings können auch über mehrere Zeilen gehen
print("""Das ist ein Text,
der über mehrere Zeilen wächst
und wächst ...""")

# Wichtige Stringfunktionen

# Konkatination
strValue = "Hello" + "World"
print("'Hello' + 'World' ->", strValue)

# Wiederholung
strValue = "x" * 3
print("'x' * 3 ->", strValue)

# Indexing
strValue = "Python"

# Strings bestehen aus einzelnen Zeichen (Character) auf die zugegriffen werden kann
print("Erstes Zeichen (Index=0) von 'Python':", strValue[0])
print("Letztes Zeichen (Index=5) von 'Python':", strValue[5])

# Die Indizierung wird in Python aber auch rückwärts durchgeführt und geht in den negativen Index-Bereich
print("Letztes Zeichen (Index=-1) von 'Python':", strValue[-1])
print("Erstes Zeichen (Index=-6) von 'Python':", strValue[-6])

# Slicing

sliceValue = strValue[2:4]
print("slice[2:4] von 'Python' ->", sliceValue)

# Länge

print("Anzahl Zeichen von 'Python':", len(strValue))

# Strings sind unveränderlich!
# So funktioniert eine Zuweisung über einen Index nicht!
# strValue[0] = 'J' -> Fehler!

# Besonderheiten bei Strings und den Referenzen auf die Objekte
# Mit dem is-Operator wird die Identität eines Objekts verglichen
# Anmerkung: Auf www.python-kurs.eu ist noch die Rede davon, dass es bei Umlauten und Sonderzeichen
# zu einem abweichenden Verhalten kommt. Das kann mit Python 3.7.4 nicht mehr nachgestellt werden.
# Es scheint also ein Bug in den früheren Versionen gewesen zu sein... 
a = "Linux"
b = "Linux"
print("a is b:", a is b)
print("a == b:", a == b)

a = "Blödsinn"
b = "Blödsinn"
print("a is b:", a is b)
print("a == b:", a == b)

a = "Linux!"
b = "Linux!"
print("a is b:", a is b)
print("a == b:", a == b)

# Operatoren

print("40 + 2 =", 40 + 2)    # Addition
print("44 - 2 =", 44 - 2)    # Subtraktion
print(" 6 * 7 =", 6 * 7)     # Multiplikation
print("10 % 3 =", 10 % 3)    # Modulo (Rest)
print("10 / 3 =", 10 / 3)    # Division
print("10 // 3 =", 10 // 3)  # Ganzzahl Division
print("2 ** 5 =", 2 ** 5)    # Exponentiation
print("Vorzeichen -1", -1)   # Negationsvorzeichen
print("boolsches 'oder': True or False =", True or False)
print("boolsches 'and': True and False =", True and False)
print("boolsches 'not': not True =", not True)
print("Vergleichsoperation '<': 1 < 2 =", 1 < 2)    # kleiner
print("Vergleichsoperation '<=': 2 <= 2 =", 2 <= 2) # kleiner gleich
print("Vergleichsoperation '>=': 2 >= 2 =", 2 >= 2) # größer gleich 
print("Vergleichsoperation '>': 3 > 2 =", 3 > 2)    # größer
print("Vergleichsoperation '==': 2 == 2 =", 2 == 2) # gleich (Wertegleichheit!)
print("Vergleichsoperation '!=': 2 != 2 =", 2 != 2) # ungleich (Wertegleichheit!)
print("Vergleichsoperation 'is': 2 is 2 =", 2 is 2) # gleich (Objekt-/Identitätsgleichheit!)

print("Bitweises not von   0b0101 (5) =", bin(~0b0101), ~0b0101)      # Bitweise Negation (Binäres Komplement)
print("Bitweises oder von  0b1100 | 0b0011 =", bin(0b1100 | 0b0011))  # Bitweises Oder
print("Bitweises und von   0b1011 & 0b1100 =", bin(0b1011 & 0b1100))  # Bitweises Und  (Maskieren)
print("Exklusives oder von 0b1101 ^ 0b0100 =", bin(0b1101 ^ 0b0100))  # Bitweises Xor  (Exklusives Oder)
print("Bitweise Shiftoperation (links) 0b0001 << 2", bin(0b0001 << 2))
print("Bitweise Shiftoperation (rechts) 0b1000 >> 2", bin(0b1000 >> 2))



