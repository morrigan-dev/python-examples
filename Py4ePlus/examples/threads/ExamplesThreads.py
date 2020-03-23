'''

@see: https://www.linkedin.com/learning/multithreading-mit-python/willkommen-zu-dem-video-training-multithreading-mit-python
'''
from examples.threads.EventHighApi import EventHighApi
from examples.threads.JoinThreadHighApi import JoinThreadHighApi
from examples.threads.LocksAndSyncLowApi import LocksAndSyncLowApi
from examples.threads.MultipleThreadsLowApi import MultipleThreadsLowApi
from examples.threads.RLockHighApi import RLockHighApi
from examples.threads.SemaphoreHighApi import SemaphoreHighApi
from examples.threads.SimpleThreadLowApi import SimpleThreadLowApi
from examples.threads.SimpleThreadsHighApi import SimpleThreadsHighApi
from examples.threads.ThreatErrorLowApi import ThreatErrorLowApi
from examples.threads.TimerHighApi import TimerHighApi

exercises = (
    SimpleThreadLowApi(),
    MultipleThreadsLowApi(),
    LocksAndSyncLowApi(),
    ThreatErrorLowApi(),
    SimpleThreadsHighApi(),
    RLockHighApi(),
    JoinThreadHighApi(),
    TimerHighApi(),
    EventHighApi(),
    SemaphoreHighApi()
)

print("Wähle eine Übung aus:")
counter = 0
for ex in exercises:
    print("{}) {}".format(counter, ex.getTitle()))
    counter += 1
print("Enter beendet das Program.")
input_value = input("Nummer der Übung: ")
if input_value.isnumeric():
    exercise_number = int(input_value)
    exercises[exercise_number].main()
