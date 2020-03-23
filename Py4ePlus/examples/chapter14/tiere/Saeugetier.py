from examples.chapter14.tiere.Tier import Tier


class Saeugetier(Tier):

    def __init__(self, alter):
        Tier.__init__(self, alter)

    def laufen(self):
        pass