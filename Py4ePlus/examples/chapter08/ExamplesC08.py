'''
Created on 10.03.2020

In diesem Modul sind Beispiele zu folgenden Themen enthalten:
- Listen

@author: morrigan
'''

# Erzeugung von Listen
int_list = [1, 2, 3]
print("int_list =", int_list)
mixed_list = ["Eine", "Liste", "mit", 5, ["I", "t", "e", "m", "s"]]
print("mixed_list =", mixed_list)
empty_list = []
print("empty_list =", empty_list)

# Listen können verändert werden
mutable_list = ["A", "B", "D"]
print("mutable_list =", mutable_list)
mutable_list[2] = "C"
print("mutable_list =", mutable_list)

# Operationen auf Listen
my_list = [0] * 4
print("my_list =", my_list)
my_list[0] = 1
print("my_list =", my_list)
my_list = ['a', 'b', 'c', 'd', 'e', 'f']
print("my_list =", my_list)
print("my_list[1:3] =", my_list[1:3])
print("my_list[:4] =", my_list[:4])
print("my_list[3:] =", my_list[3:])
print("my_list[:] =", my_list[:])

# Methoden auf Listen
my_list = ['a', 'b', 'c']
print("my_list =", my_list)
my_list.append("d")
print("my_list =", my_list)
my_list.extend(['e', 'f'])
print("my_list =", my_list)
my_list.sort(reverse=True)
print("my_list =", my_list)
item = my_list.pop(1)
print("my_list = {}, item = {}".format(my_list, item))
del my_list[0]
print("my_list =", my_list)
my_list.remove('d')
print("my_list =", my_list)

# Functionen für Listen
nums = [3, 41, 12, 9, 74, 15]
print("len(nums) =", len(nums))
print("max(nums) =", max(nums))
print("min(nums) =", min(nums))
print("sum(nums) =", sum(nums))
print("sum(nums)/len(nums) =", sum(nums) / len(nums))

# Listen mit Strings
words = "what a beautiful day"
splitted_words = words.split()
print("splitted_words =", splitted_words)
delimiter = "_"
new_words = delimiter.join(splitted_words)
print("new_words =", new_words)

# Objekte und Werte
a = "banana"
b = "banana"
print("a = {}, b = {} -> a is b = {}".format(a, b, a is b))

a = [1, 2, 3]
b = [1, 2, 3]
print("a = {}, b = {} -> a is b = {}".format(a, b, a is b))

# Listen werden bei Funktionen referenziert
def delete_head(t):
    del t[0]
letters = ['a', 'b', 'c']
print("letters =", letters)  
delete_head(letters)
print("letters =", letters)  



