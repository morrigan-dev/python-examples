from examples.chapter14.tiere.Tier import Tier


class Vogel(Tier):

    def __init__(self, alter):
        Tier.__init__(self, alter)

    def fliegen(self):
        pass

    def lautgeben(self):
        print("Piep")