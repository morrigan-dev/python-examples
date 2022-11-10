'''
Created on 17.03.2020

In diesem Modul sind Beispiele zu folgenden Themen enthalten:
- Netzwerk Programmierung

@author: morrigan
@see: https://www.py4e.com/html3/12-network
'''
import re
import socket
import ssl
import urllib.request

#from bs4 import BeautifulSoup

# Text über eine URL aufrufen mit Sockets
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")
mysock.close()
print()

# Bild über eine URL aufrufen mit Sockets
HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""
while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    #time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data
mysock.close()
print()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
with open("stuff.jpg", "wb") as file_handle:
    file_handle.write(picture)
print()

# Text über eine URL aufrufen mit urllib
with urllib.request.urlopen('http://data.pr4e.org/romeo.txt') as file_handle:
    for line in file_handle:
        print(line.decode().strip())
print()

# Bild mittels urllib öffenen und speichern
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
with open('cover3.jpg', 'wb') as file_handle:
    file_handle.write(img)


# Parsen von URLs

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1: url = "https://docs.python.org"
html = urllib.request.urlopen(url).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())


# Nutzung von BeautifulSoup zum Parsen von fehlerhaftem HTML
url = input('Enter - ')
if len(url) < 1: url = "https://docs.python.org"
html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, "html.parser")
# Retrieve all of the anchor tags
#tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))