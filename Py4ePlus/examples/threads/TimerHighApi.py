import threading as t


class TimerHighApi:

    def getTitle(self):
        return "Threads - Timer High Api"

    def main(self):
        def a():
            print("A")

        def b():
            print("B")

        def c():
            print("C")

        def d():
            print("D")

        def e():
            print("E")
            t4.cancel()

        t1 = t.Timer(2.0, a)
        t2 = t.Timer(6.0, c)
        t3 = t.Timer(4.0, b)
        t4 = t.Timer(10.0, d)
        t5 = t.Timer(8.0, e)
        t1.start()
        t3.start()
        t2.start()
        t4.start()
        t5.start()


if __name__ == '__main__':
    TimerHighApi().main()