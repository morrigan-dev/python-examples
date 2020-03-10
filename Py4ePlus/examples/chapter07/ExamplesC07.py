'''
Created on 10.03.2020

In diesem Modul sind Beispiele zu folgenden Themen enthalten:
- Dateiinhalte lesen
- Dateiinhalte schreiben

@author: morrigan
@see: https://www.py4e.com/html3/07-files
'''
from examples import DATA_PATH
from examples import print_header

print_header("Kapitel 7 - Dateiinhalte lesen")

# Öffnen einer Datei, die im 'data' Verzeichnis liegt
fileHandle = open(DATA_PATH / "mbox.txt")
print("fileHandle =", fileHandle)
fileHandle.close()
print()

# Zeilen einer Datei ermitteln
fileHandle = open(DATA_PATH / "mbox-short.txt")
count = 0
for line in fileHandle:
    count += 1
fileHandle.close()    
print("Es wurden {} Zeilen gefunden.".format(count))    
print()

# Einlesen einer kompletten Datei und Anzahl der Zeichen ermitteln
fileHandle = open(DATA_PATH / "mbox-short.txt")
fileContent = fileHandle.read()
print("Es wurden {} Zeichen gefunden.".format(len(fileContent)))
fileHandle.close()
print()

# Suche in einer Datei
fileHandle = open(DATA_PATH / "mbox-short.txt")
for line in fileHandle:
    if(line.startswith("From:")):
        print(line.rstrip())
fileHandle.close()
print()

print_header("Kapitel 7 - Dateiinhalte schreiben")

# Schreiben in Dateien
fileHandle = open(DATA_PATH / "output.txt", "w")
fileHandle.write("Eine neue Zeile in eine Datei schreiben")
fileHandle.close()
print("Zeile wurde erfolgreich in 'output.txt' geschrieben.")
print()

# Dateibehandlung mit automatischem Schließen
print("Dateiinhalt von 'output':")
with open(DATA_PATH / "output.txt") as f:
    for line in f:
        print(line)
print()



