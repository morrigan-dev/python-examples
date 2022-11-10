from examples.chapter14.tiere.Tier import Tier
from examples.chapter14.tiere.Katze import Katze
from examples.chapter14.tiere.Vogel import Vogel
from examples.chapter14.tiere.Hund import Hund


class Tierprogramm:
    def main(self):
        print("Anzahl der Tiere:", Tier.AnzahlTiere())
        susi = Tier()
        print("Anzahl der Tiere:", Tier.AnzahlTiere())
        strolch = Tier()
        print("Anzahl der Tiere:", Tier.AnzahlTiere())
        herb = Tier()
        print("Anzahl der Tiere am Ende (Abfrage für die Klasse):", Tier.AnzahlTiere())
        print("Anzahl der Tiere am Ende (Abfrage für die Klasse):", susi.AnzahlTiere())

        mopsi = Tier.ErzeugeTier()
        print("Anzahl der Tiere am Ende (Abfrage nach statischer Methode):", Tier.AnzahlTiere())

        katze = Katze(1, "Susi", "Neustadt", "Bibi")
        print(katze.alter)
        katze.alter = 2
        print(katze.alter)
        kater = Katze(1, "Strolch", "Neustadt", "Bibi")
        print(kater.name)

        katze = Katze(1, "Susi", "Neustadt", "Bibi")
        vogel = Vogel(3)
        hund = Hund(2)
        hund.bellen()
        katze.miauen()
        print(vogel.alter)
        vogel.lautgeben()
        katze.lautgeben()
        hund.lautgeben()

    def __init__(self):
        Tierprogramm.main(self)




