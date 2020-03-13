'''
Created on 12.03.2020

In diesem Modul sind Beispiele zu folgenden Themen enthalten:
- Tuple

@author: morrigan
@see: https://www.py4e.com/html3/10-tuples
'''

import string

from examples import DATA_PATH
from examples import print_header

print_header("Kapitel 10 - Tuple")

# Erzeugung von Tuple
t = ("a", "b", "c", "d", "e")
tuple_with_one_item = ("a",)
simple_string = ("a")
print("t = {}".format(t))
print("simple_string = {} {}".format(type(simple_string), simple_string))
print("tuple_with_one_item = {} {}".format(type(tuple_with_one_item), tuple_with_one_item))
print()

# Vergleich von Tupeln
print("(0, 1, 2) < (0, 3, 4) =", (0, 1, 2) < (0, 3, 4))
print("(0, 1, 2000000) < (0, 3, 4) =", (0, 1, 2000000) < (0, 3, 4))
print()

# Sortieren von Tupeln
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
t.sort(reverse=True)
res = list()
for length, word in t:
    res.append(word)
print(res)
print()

# Zuweisung von Tupeln
m = ["have", "fun"]
(x, y) = m
print("m =", m)
print("x =", x)
print("y =", y)
(x, y) = (y, x)
print("x =", x)
print("y =", y)
addr = 'monty@python.org'
uname, domain = addr.split('@')
print("addr =", addr)
print("uname =", uname)
print("domain =", domain)
print()

# Dictionaries und Tuple
d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print(t)
print()

fhand = open(DATA_PATH / 'romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)