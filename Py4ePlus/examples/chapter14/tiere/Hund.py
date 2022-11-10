from examples.chapter14.tiere.Saeugetier import Saeugetier


class Hund(Saeugetier):

    def __init__(self, alter):
        Saeugetier.__init__(self, alter)

    def lautgeben(self):
        self.bellen()

    def bellen(self):
        print("Wau")