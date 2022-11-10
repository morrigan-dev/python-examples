import threading as t
import time as z


class EventHighApi:

    class MyThread1(t.Thread):

        def __init__(self):
            t.Thread.__init__(self)
            self.daemon = False

        def run(self):
            print("Start", str(self))
            self.do_something()
            print("Ende", str(self))

        def do_something(self):
            while True:
                z.sleep(2)
                print(self.ident, evt.is_set())
                evt.wait()
                if(evt.is_set()):
                    print("Botschaft bekommen")
                    break

    class MyThread2(t.Thread):

        def __init__(self):
            t.Thread.__init__(self)
            self.daemon = False

        def run(self):
            print("Start", str(self.ident))
            self.do_something()
            print("Ende", str(self.ident))

        def do_something(self):
            z.sleep(10)
            print("Sende Botschaft")
            evt.set()

    def getTitle(self):
        return "Threads - Event High Api"

    def main(self):
        t1.start()
        t2.start()


t1 = EventHighApi.MyThread1()
t2 = EventHighApi.MyThread2()
evt = t.Event()

if __name__ == '__main__':
    EventHighApi().main()