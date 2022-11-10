import threading as t
import time


class SimpleThreadsHighApi:

    lock = t.Lock()

    class MyThread(t.Thread):


        def __init__(self, thread_id, name, delay, counter):
            t.Thread.__init__(self)
            self.__thread_id = thread_id
            self.__name = name
            self.__delay = delay
            self.__counter = counter
            self.__i = 0

        def run(self) -> None:
            SimpleThreadsHighApi.lock.acquire()
            print("Start {}".format(self.__name))
            SimpleThreadsHighApi.lock.release()
            self.do_something()
            SimpleThreadsHighApi.lock.acquire()
            print("Ende {}".format(self.__thread_id))
            SimpleThreadsHighApi.lock.release()

        def do_something(self):
            self.__i = 0
            while self.__i < self.__counter:
                SimpleThreadsHighApi.lock.acquire()
                self.__i += 1
                print(self.__name, self.__thread_id, self.__i, "/", self.__counter)
                SimpleThreadsHighApi.lock.release()
                time.sleep(self.__delay)

    def getTitle(self):
        return "Threads - Threads mit 'High Level API'"

    def main(self):
        t1 = self.MyThread(4711, "Thread-1", 2, 4)
        t2 = self.MyThread(4712, "Thread-2", 3, 7)

        t1.start()
        t2.start()


if __name__ == '__main__':
    SimpleThreadsHighApi().main()