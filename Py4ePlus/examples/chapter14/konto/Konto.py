class Konto:

    def __init__(self, kontostand, kontotyp):
        self._kontostand = kontostand
        self.kontotyp = kontotyp

    def __del__(self):
        print("Konto wurde gelöscht")

    def getKontostand(self):
        return self._kontostand

    def einzahlen(self, betrag):
        self._kontostand += betrag

    def auszahlen(self, betrag):
        self._kontostand -= betrag