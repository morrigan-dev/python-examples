import _thread
import time

from examples import print_header


class SimpleThreadLowApi:

    def __init__(self):
        self.__stop = False

    def getTitle(self):
        return "Threads - Einfacher Thread mit 'Low Level API'"

    # Funktion, die als Thread ausgeführt werden soll
    def ausgabe_zeit(self, threadName, delay):
        count = 0
        while count < 10:
            time.sleep(delay)
            count += 1
            print(count)
            if self.__stop: _thread.exit()

    def main(self):

        print_header(self.getTitle())

        # Erstellung eines Threads
        try:
            _thread.start_new_thread(self.ausgabe_zeit, ("Mein-Thread-1", 1,))
        except:
            print("Fehler beim Start eines Threads")

        # Main-Thread soll nicht beendet werden
        print("Enter Drücken, um Beispiel abzubrechen")
        while True:
            if not input():
                self.__stop = True
                break
        print("Beispiel wurde abgebrochen")
        print()
