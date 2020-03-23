from examples.chapter14.konto.Kunde import Kunde
from examples.chapter14.konto.Konto import Konto
from examples.chapter14.konto.KontoMitSlots import KontoMitSlots


class Bankenprogramm:

    def konto_zuruecksetzen(self):
        self.auszahlen(self.getKontostand())

    def main(self):
        konto2 = Konto(1, "")

        kunde = Kunde("Hans", "Dampf", 42, "männlich", "Mustermannstr. 1 12345 Beispielhausen", Konto(1000, "Girokontot"))
        konto = kunde.getKonto()
        del konto2
        print(konto)
        print(konto.getKontostand())
        konto.einzahlen(123)
        print(konto.getKontostand())
