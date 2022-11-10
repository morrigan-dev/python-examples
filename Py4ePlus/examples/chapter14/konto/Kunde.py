class Kunde:

    def __init__(self, vorname, nachname, alter, geschlecht, adresse, konto):
        self.__vorname = vorname
        self.__nachname = nachname
        self.__alter = alter
        self.__geschlecht = geschlecht
        self.__adresse = adresse
        self.__konto = konto

    def __del__(self):
        print("Kunde {} {} wurde gelöscht.".format(self.__vorname, self.__nachname))
    def getKonto(self):
        return self.__konto;
