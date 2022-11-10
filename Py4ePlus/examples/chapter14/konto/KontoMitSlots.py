class KontoMitSlots():
    __slots__ = ["__kontostand", "kontotyp"]

    def __init__(self, kontostand, kontotyp):
        self.__kontostand = kontostand
        self.kontotyp = kontotyp

    def __del__(self):
        print("Konto wurde gelöscht")

    def getKontostand(self):
        return self.__kontostand

    def einzahlen(self, betrag):
        self.__kontostand += betrag

    def auszahlen(self, betrag):
        self.__kontostand -= betrag