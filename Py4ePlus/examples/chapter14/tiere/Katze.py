from examples.chapter14.tiere.Saeugetier import Saeugetier
from examples.chapter14.konto.Eigentuemer import Eigentuemer


class Katze(Saeugetier, Eigentuemer):
    def __init__(self, alter, name, wohnort, person):
        Saeugetier.__init__(self, alter)
        Eigentuemer.__init__(self, wohnort, person)
        self.__name = name

    def __getName(self):
        return self.__name
    name = property(__getName)

    def lautgeben(self):
        self.miauen()

    def miauen(self):
        print("Miau")