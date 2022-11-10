import threading as t
import time as z

class JoinThreadHighApi():

    class Thread1(t.Thread):
        def __init__(self):
            t.Thread.__init__(self)

        def run(self):
            print("Start", str(self))
            self.do_something()
            print("Ende", str(self))

        def do_something(self):
            z.sleep(3)
            print("t1 join t2")
            t2.join()
            print("t1 zurück von t2")

    class Thread2(t.Thread):
        def __init__(self):
            t.Thread.__init__(self)

        def run(self):
            print("Start", str(self))
            self.do_something()
            print("Ende", str(self))

        def do_something(self):
            i = 0
            print("t2 aktiv")
            z.sleep(5)
            while i < 5:
                i += 1
                print(i)
                z.sleep(1)

    def getTitle(self):
        return "Threads - Join mit High Api"

    def main(self):
        t1.start()
        t2.start()


t1 = JoinThreadHighApi.Thread1()
t2 = JoinThreadHighApi.Thread2()

if __name__ == '__main__':
    JoinThreadHighApi().main()