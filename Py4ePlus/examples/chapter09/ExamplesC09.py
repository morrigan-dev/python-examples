'''
Created on 10.03.2020

In diesem Modul sind Beispiele zu folgenden Themen enthalten:
- Dictionaries

@author: morrigan
@see: https://www.py4e.com/html3/09-dictionaries
'''
import string

from examples import DATA_PATH
from examples import print_header

print_header("Kapitel 9 - Dictionaries")

# Erstellung eines neuen Dictionaries
eng2sp = dict()
eng2sp["one"] = "uno"
print("eng2sp = {}".format(eng2sp))
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print("eng2sp = {}".format(eng2sp))
print("eng2sp['two'] = {}".format(eng2sp["two"]))
print("len(eng2sp) = {}".format(len(eng2sp)))
print("'one' in eng2sp = {}".format("one" in eng2sp))
print("'uno' in eng2sp = {}".format("uno" in eng2sp))
values = eng2sp.values()
print("values = {}".format(values))
print("'uno' in values = {}".format("uno" in values))

# Zählen mit Hilfe von Dictionaries
word = 'brontosaurus'
my_dict = dict()
for letter in word:
    if letter not in my_dict:
        my_dict[letter] = 1
    else:
        my_dict[letter] = my_dict[letter] + 1
print(my_dict)
print("my_dict['o'] =", my_dict["o"])
for key in my_dict:
    print(key, my_dict[key])

# Fortgeschrittene Textanalyse
with open(DATA_PATH / "words.txt") as file_handle:
    counts = dict()
    for line in file_handle:
        line = line.rstrip()
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
    print(counts)
