class Tier:
    anzahl = 0

    # magic Methode mit optionalem Parameter für die Initialisierung die nach dem Konstruktor aufgerufen wird
    def __init__(self, alter=0):
        # Alter mit der Sichtbarkeit Protected (Achtung! Nur Konvention. Zugriff ist dennoch möglich)
        self._alter = alter
        Tier.anzahl += 1

    # Statische Methode der Klasse ohne Bezug zur Klasse
    @staticmethod
    def ErzeugeTier():
        return Tier()

    # Klassenmethode mit Bezug zur Klasse
    @classmethod
    def AnzahlTiere(cls):
        return cls.anzahl

    # Privater Getter für den privaten Member __alter
    def __getAlter(self):
        return self._alter

    # Privater Setter für den privaten Member __alter
    def __setAlter(self, alter):
        self._alter = alter

    # Property für den privaten Member __alter
    alter = property(__getAlter, __setAlter)

    def lautgeben(self):
        print("Stille")
