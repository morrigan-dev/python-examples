import threading as t
import time as z


class ConditionHighApi:

    def getTitle(self):
        return "Threads - Conditions High Api"

    def wartenderThread(self, cv):
        print("wartenderThread gestartet ...")
        with cv:
            cv.wait()
            print("wartender Thread kann nun weiterarbeiten")

    def freigegebenerThread(self, cv):
        print("freigegebenerThread gestartet ...")
        z.sleep(1)
        print("Arbeitet irgendwelche Sachen")
        z.sleep(1)
        print("Informiert alle wartenden Threads")
        with cv:
            cv.notifyAll()

    def main(self):
        condition = t.Condition()
        w1 = t.Thread(target=self.wartenderThread, args=(condition,))
        w2 = t.Thread(target=self.wartenderThread, args=(condition,))
        w3 = t.Thread(target=self.wartenderThread, args=(condition,))
        w4 = t.Thread(target=self.wartenderThread, args=(condition,))
        fg = t.Thread(target=self.freigegebenerThread, args=(condition,))

        w1.start()
        z.sleep(2)
        w2.start()
        z.sleep(2)
        w3.start()
        z.sleep(2)
        w4.start()
        z.sleep(2)

        fg.start()

if __name__ == '__main__':
    ConditionHighApi().main()