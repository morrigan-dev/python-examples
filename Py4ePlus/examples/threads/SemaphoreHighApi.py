import threading as t
import time as z

class SemaphoreHighApi:

    class MyThread1(t.Thread):
        lock = t.Semaphore(3)

        def run(self):
            SemaphoreHighApi.MyThread1.lock.acquire()
            self.do_something()

        def do_something(self):
            print(self.ident)
            z.sleep(5)
            SemaphoreHighApi.MyThread1.lock.release()

    class MyThread2(t.Thread):
        bar = t.Barrier(3)

        def run(self):
            SemaphoreHighApi.MyThread2.bar.wait()
            self.do_something()

        def do_something(self):
            print("Barriere überwunden")

    def getTitle(self):
        return "Threads - Semaphore und Barrier High Api"

    def main(self):
        threads = []
        for i in range(0, 10):
            threads.append(SemaphoreHighApi.MyThread1())
        for thread in threads:
            thread.start()

        input("Enter für nächsten Schritt")

        threads.clear()
        for i in range(0, 5):
            threads.append(SemaphoreHighApi.MyThread2())
        for thread in threads:
            thread.start()


if __name__ == '__main__':
    SemaphoreHighApi().main()