class Eigentuemer:

    def __init__(self, wohnort, person):
        self.__wohnort = wohnort
        self.__person = person

    def __getWohnort(self):
        return self.__wohnort
    def __setWohnort(self, wohnort):
        self.__wohnort = wohnort
    wohnort = property(__getWohnort, __setWohnort)

    def __getPerson(self):
        return self.__person
    def __setPerson(self, person):
        self.__person = person
    person = property(__getPerson, __setPerson)