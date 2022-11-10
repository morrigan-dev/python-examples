import _thread
import time

from examples import print_header


class LocksAndSyncLowApi:

    def __init__(self):
        self.__daten = 0
        # Lock-Objekt für die Synchronisation
        self.lock = _thread.allocate_lock()

    def getTitle(self):
        return "Threads - Locks und Synchronisation mit 'Low Level API'"

    # Funktion, die als Thred ausgeführt werden soll
    def synced_ausgabe(self, thread_name, delay):
        count = 0
        while count < 10:
            self.lock.acquire()
            count += 1 # nicht atomar!
            self.__daten += 1 # nicht atomar!
            print("Thread: {}, globale Daten: {}".format(thread_name, self.__daten)) # nicht atomar!
            self.lock.release()

    def main(self):
        print("Enter Drücken, um Beispiel abzubrechen")

        # Erstellung eines Threads
        try:
            _thread.start_new_thread(self.synced_ausgabe, ("Mein-Thread-1", 1, ))
            _thread.start_new_thread(self.synced_ausgabe, ("Mein-Thread-2", 2, ))
            _thread.start_new_thread(self.synced_ausgabe, ("Mein-Thread-3", 5, ))
        except:
            print("Fehler beim Start eines Threads")

        print("Enter Drücken, um Beispiel abzubrechen")
        while True:
            if not input(): break
        print("Beispiel wurde abgebrochen")
        print()
