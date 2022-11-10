import _thread
import time


class ThreatErrorLowApi:

    def __init__(self):
        # Lock-Objekt für die Synchronisation
        self.__lock = _thread.allocate_lock()

    def getTitle(self):
        return "Threads - Error/Abbruch in einem Thread mit 'Low Level API'"

    # Funktion, die als Thred ausgeführt werden soll
    def error_ausgabe(self, thread_name, ball):
        count = 0

        while count < 10:
            self.__lock.acquire()
            count += 1
            print("Thread: {}, Thread ID: {}, stack size: {}, locked: {}, count: {}"
                  .format(thread_name, _thread.get_ident(), _thread.stack_size(), self.__lock.locked(), count))
            self.__lock.release()
            time.sleep(1)
            if count > 5 and ball == 0:
                raise _thread.error

    def main(self):
        print("Enter Drücken, um Beispiel abzubrechen")

        # Erstellung eines Threads
        try:
            _thread.start_new_thread(self.error_ausgabe, ("Mein-Thread-1", 0,))
            _thread.start_new_thread(self.error_ausgabe, ("Mein-Thread-2", 1,))
        except:
            print("Fehler beim Start eines Threads")

        while True:
            if not input(): break
        print("Beispiel wurde abgebrochen")
        print()