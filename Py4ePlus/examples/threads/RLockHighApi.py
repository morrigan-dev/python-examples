import threading as t
import time as z


class RLockHighApi(t.Thread):
    lock = t.RLock()
    i = 0

    def __init__(self):
        t.Thread.__init__(self)

    def run(self):
        RLockHighApi.lock.acquire()
        print("Start", str(self.name))
        RLockHighApi.lock.release()

        z.sleep(1)

        RLockHighApi.lock.acquire()
        self.do_something()
        RLockHighApi.lock.release()

        RLockHighApi.lock.acquire()
        print("Ende", str(self.name))
        RLockHighApi.lock.release()

    def do_something(self):
        while True:
            if self.name == "Thread-2":
                RLockHighApi.i += 1
            else:
                RLockHighApi.i -= 1
            print(self.name, RLockHighApi.i)
            z.sleep(1)
            if RLockHighApi.i > 10 or RLockHighApi.i < 0:
                break

    def getTitle(self):
        return "Threads - RLock mit High Api"

    def main(self):
        t1 = RLockHighApi()
        t2 = RLockHighApi()
        t3 = RLockHighApi()
        t4 = RLockHighApi()
        t1.start()
        t2.start()
        t3.start()
        t4.start()

if __name__ == '__main__':
    RLockHighApi().main()