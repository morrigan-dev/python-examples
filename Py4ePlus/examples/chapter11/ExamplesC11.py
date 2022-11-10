'''
Created on 12.03.2020

In diesem Modul sind Beispiele zu folgenden Themen enthalten:
- Reguläre Ausdrücke

@author: morrigan
@see: https://www.py4e.com/html3/11-regex
@see: https://www.python-kurs.eu/python3_re.php
@see: https://www.python-kurs.eu/python3_re_fortgeschrittene.php
'''
import re

# Schreibweise von Regulären Ausdrücken
regex = "^a.*\\.html$"  # Backslash wird escaped
regex2 = r"^a.*\.html$"  # Backslash muss nicht escaped werden da ein raw string genutzt wird

# Einfaches Beispiel einer regulären suche
print(re.search("cat", "A cat and a rat can't be friends."))
print(re.search("cow", "A cat and a rat can't be friends."))
print()

# Beliebiges Zeichen
print(re.findall(" .at ", "A cat and a rat can't be friends. @at - 3at "))
print()

# Zeichenauswahl
print(re.findall("[a-z]", "A cat and a rat can't be friends. @at - 3at "))
print(re.findall("[-a-z]", "A cat and a rat can't be friends. @at - 3at "))
print(re.findall("[^a-z]", "A cat and a rat can't be friends. @at - 3at "))
print()

# Vordeinierte Zeichen
text = "A cat and a rat can't be friends. @at - 3at "
print(text)
print("'\d' ->", re.findall(r"\d", text))  # => [0-9]
print("'\D' ->", re.findall(r"\D", text))  # => ^[0-9]
print("'\s' ->", re.findall(r"\s", text))  # => [\t\n\r\f\v]
print("'\D' ->", re.findall(r"\S", text))  # => ^[\t\n\r\f\v]
print("'\w' ->", re.findall(r"\w", text))  # => [a-zA-Z0-9_]
print("'\W' ->", re.findall(r"\W", text))  # => ^[a-zA-Z0-9_]
print()

# Wortbegrenzer
text = "A  cat and a rat!"
print(text)
print(r"'^' ->", re.search(r"^", text))
print(r"'\A' ->", re.search(r"\A", text))
print(r"'\b' ->", re.search(r"\b", text))
print(r"'\B' ->", re.search(r"\B", text))
print(r"'\Z' ->", re.search(r"\Z", text))
print(r"'$' ->", re.search(r"$", text))
print()

# Beispiele mit den verschiedenen Formen von Meier
s1 = "Mayer ist ein verbreiteter Name"
s2 = "Er heißt Mayer, ist aber nicht Deutscher."
print("s1 =", s1)
print("s2 =", s2)
print("s1.search -> 'M[ae][iy]er' =", re.search(r"M[ae][iy]er", s1))
print("s2.search -> 'M[ae][iy]er' =", re.search(r"M[ae][iy]er", s2))
print("s1.match -> 'M[ae][iy]er' =", re.match(r"M[ae][iy]er", s1))
print("s2.match -> 'M[ae][iy]er' =", re.match(r"M[ae][iy]er", s2))
print("s1.search -> '^M[ae][iy]er' =", re.search(r"^M[ae][iy]er", s1))
print("s2.search -> '^M[ae][iy]er' =", re.search(r"^M[ae][iy]er", s2))
s = s2 + "\n" + s1
print(s)
print("s.search -> '^M[ae][iy]er' =", re.search(r"^M[ae][iy]er", s))
print("s.search -> '^M[ae][iy]er' (multiline) =", re.search(r"^M[ae][iy]er", s, re.MULTILINE))
print("s.match -> '^M[ae][iy]er' (multiline) =", re.match(r"^M[ae][iy]er", s, re.MULTILINE))
s = "Mayer, ist nicht gleich Meier aber im Ausland könnte es auch Meir heißen."
print(s)
print("s.findall -> '^M[ae][iy]e?r' =", re.findall(r"M[ae][iy]e?r", s))
print()

# Quantoren
value = "Wert: 12345"
print(value)
print("findall -> '[0-9]*' =", re.findall(r"[0-9]*", value))

# TODO: Weitere Beispiele hinzufügen ...
# https://www.python-kurs.eu/python3_re.php
# https://www.python-kurs.eu/python3_re_fortgeschrittene.php
