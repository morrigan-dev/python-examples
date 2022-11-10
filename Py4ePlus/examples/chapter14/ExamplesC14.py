'''
Created on 19.03.2020

In diesem Modul sind Beispiele zu folgenden Themen enthalten:
- Objektorientierte Programmierung

@author: morrigan
@see: https://www.py4e.com/html3/14-objects
@see: https://www.linkedin.com/learning/oop-mit-python/willkommen-zu-oop-mit-python
'''
from examples.chapter14.konto.Bankenprogramm import Bankenprogramm
from examples.chapter14.konto.Konto import Konto
from examples.chapter14.konto.KontoMitSlots import KontoMitSlots
from examples.chapter14.tiere.Tierprogramm import Tierprogramm
from examples.chapter14.tiere.Tier import Tier
from copy import copy
from copy import deepcopy


class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


animal = PartyAnimal()
animal.party()
animal.party()
animal.party()
PartyAnimal.party(animal)

Tierprogramm()

prog = Bankenprogramm()
prog.main()

konto = Konto(1000, "Girokonto")
print("Das Dictionary __dict___:", konto.getKontostand(), konto.__dict__)
konto.eigentuemer = "Thomas"
print("Das Dictionary __dict___:", konto.getKontostand(), konto.__dict__)
konto.zuruecksetzen = Bankenprogramm.konto_zuruecksetzen
print("Das Dictionary __dict___:", konto.getKontostand(), konto.__dict__)
konto.zuruecksetzen(konto)
print("Das Dictionary __dict___:", konto.getKontostand(), konto.__dict__)
konto.getTyp = lambda: konto.kontotyp
print("Das Dictionary __dict___:", konto.getTyp(), konto.__dict__)

unveraenderlichesKonto = KontoMitSlots(1000, "Girokonto")
try:
    print("__dict___:", unveraenderlichesKonto.__dict__)
except AttributeError as e:
    print(e)
print("__slots__", unveraenderlichesKonto.__slots__)

# Dynamisch erzeugte Klassen zur Laufzeit
DynamicClassTier = type("Tier", (), {"alter": 3})
tier = DynamicClassTier()
print("Typ der Klasse: {}, Alter: {}".format(type(tier), tier.alter))

# Kopieren / Klonen von Objekten
t1 = Tier(2)
print(t1.alter)
t2 = t1
t3 = copy(t1)
t4 = deepcopy(t1)
t2.alter = 3
print(t1.alter)
t3.alter = 4
print(t1.alter)
t4.alter = 5
print(t1.alter)

