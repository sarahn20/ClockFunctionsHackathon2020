import time
import Enum
​
class Stopwatch(enum.Enum):
    def __init__(self):
        self.end_time = 0
        self.counter = 0
​
    def start(self):
        start_time = time.time()
        while end_time == 0:
            m, s = divmod(self.counter, 60)
            h, m = divmod(m, 60)
            running_time = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
            print(running_time + "\r", end="")
            self.counter += 1
            time.sleep(1)
​
    def stop(self):
        self.end_time = time.time()
​
class Timer(enum.Enum):
    def __init__(self, userSeconds):
        self.userSeconds = userSeconds
​
    def start(self):
        while True:
          try:
              when_to_stop = abs(int(self.userSeconds))
          except KeyboardInterrupt:
              break
          while when_to_stop > 0:
              m, s = divmod(when_to_stop, 60)
              h, m = divmod(m, 60)
              time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
              print(time_left + "\r", end="")
              time.sleep(1)
              when_to_stop -= 1
          print("00:00:00")
          break
