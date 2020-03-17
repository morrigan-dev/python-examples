'''
Created on 17.03.2020

Hier werden die Aufgaben aus dem Kurs 'Python for everbody - Kapitel 12' gelöst.

@author: morrigan
@see: https://www.py4e.com/html3/12-network
'''
import socket
import urllib
import urllib.request
from typing import re

from examples import print_exercise
from examples import print_header

print_header("Python for everybody - Kapitel 12 - Exercises")

# Exercise 1
task = """Exercise 1: Change the socket program 'socket1.py' to prompt the user for the URL so it can read any web page.
You can use 'split('/')' to break the URL into its component parts so you can extract the host name for the socket
'connect' call. Add error checking using 'try' and 'except' to handle the condition where the user enters an improperly
formatted or non-existent URL."""
print_exercise(task)

domain = None
url = input("Enter a url: ")
if len(url) < 1:
    url = "http://data.pr4e.org/romeo.txt"
    domain = "data.pr4e.org"
else:
    url_parts = url.split("/")
    if len(url_parts) >= 2 and len(url_parts[2]) > 0:
        domain = url_parts[2]
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysock:
        mysock.connect((domain, 80))
        cmd = "GET {} HTTP/1.0\r\n\r\n".format(url).encode()
        mysock.send(cmd)
        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            print(data.decode(), end='')
except InterruptedError as e:
    print(e)
print()

# Exercise 2
task = """Exercise 2: Change your socket program so that it counts the number of characters it has received and stops 
displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count 
the total number of characters and display the count of the number of characters at the end of the document."""
print_exercise(task)

content = ""
char_counter = 0
domain = None
url = input("Enter a url: ")
if len(url) < 1:
    url = "http://data.pr4e.org/romeo.txt"
    domain = "data.pr4e.org"
else:
    url_parts = url.split("/")
    if len(url_parts) >= 2 and len(url_parts[2]) > 0:
        domain = url_parts[2]
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysock:
        mysock.connect((domain, 80))
        cmd = "GET {} HTTP/1.0\r\n\r\n".format(url).encode()
        mysock.send(cmd)
        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            content = "".join([content, data.decode()])
except InterruptedError as e:
    print(e)
content_len = len(content)
max_output_len = 3000
if content_len < max_output_len:
    max_output_len = content_len
print(content[:max_output_len])
print("Gesamtanzahl an Zeichen:", content_len)
print()

# Exercise 3
task = """Exercise 3: Use urllib to replicate the previous exercise of 
(1) retrieving the document from a URL, 
(2) displaying up to 3000 characters, and 
(3) counting the overall number of characters in the document. 
Don't worry about the headers for this exercise, simply show the first 3000 characters of the document contents."""
print_exercise(task)

content = ""
with urllib.request.urlopen("http://data.pr4e.org/romeo.txt") as response:
    print(response)
    for line in response:
        content = "".join([content, line.decode()])
content_len = len(content)
max_output_len = 3000
if content_len < max_output_len:
    max_output_len = content_len
print(content[:max_output_len])
print("Gesamtanzahl an Zeichen:", content_len)
print()

# Exercise 4
task = """Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved 
HTML document and display the count of the paragraphs as the output of your program. 
Do not display the paragraph text, only count them. Test your program on several small web pages as well as some 
larger web pages."""
print_exercise(task)
print("Nicht möglich ohne BeautifulSoup Lib!")
print()

# Exercise 5
task = """Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers 
and a blank line have been received. Remember that recv receives characters (newlines and all), not lines."""
print_exercise(task)
print_content = False
domain = None
url = input("Enter a url: ")
if len(url) < 1:
    url = "http://data.pr4e.org/romeo.txt"
    domain = "data.pr4e.org"
else:
    url_parts = url.split("/")
    if len(url_parts) >= 2 and len(url_parts[2]) > 0:
        domain = url_parts[2]
content = ""
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysock:
        mysock.connect((domain, 80))
        cmd = "GET {} HTTP/1.0\r\n\r\n".format(url).encode()
        mysock.send(cmd)
        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            recv_content = data.decode()
            index = recv_content.find("\r\n\r\n")
            if print_content:
                content = "".join([content, recv_content])
            if index >= 0 and not print_content:
                print("Header Ende gefunden:", index)
                print_content = True
                content = "".join([content, recv_content[index + 4:]])
except InterruptedError as e:
    print(e)
print(content)