import _thread

from examples import print_header


class MultipleThreadsLowApi:

    def __init__(self):
        self.__counter = 0

    def getTitle(self):
        return "Threads - Mehrere Threads mit 'Low Level API'"

    # Funktion, die als Thread ausgeführt werden soll
    def ausgabe(self, threadName, delay):
        count = 0
        while count < 10:
            #time.sleep(delay)
            count += 1
            self.__counter += 1
            print("Thread: {}, Anzahl Aufrufe aller Thread: {}, Aufrufe aktueller Thread: {}"
                  .format(threadName, self.__counter, count))

    def main(self):

        print_header(self.getTitle())

        # Erstellung eines Threads
        try:
            _thread.start_new_thread(self.ausgabe, ("Mein-Thread-1", 1, ))
            _thread.start_new_thread(self.ausgabe, ("Mein-Thread-2", 2, ))
            _thread.start_new_thread(self.ausgabe, ("Mein-Thread-3", 5, ))
        except:
            print("Fehler beim Start eines Threads")

        print("Enter Drücken, um Beispiel abzubrechen")
        while True:
            if not input(): break
        print("Beispiel wurde abgebrochen")
        print()



