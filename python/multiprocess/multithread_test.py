#!/usr/local/bin/python3

import pprint
import time
import threading

class CalcQueue:
  def __init__(self, queue):
    self.queue = queue
    self.results = []
    self.num = 0

  def calc_last(self):
    self.num = self.num + 1
    num = str(self.num)
    calcs = 0
    while len(self.queue) != 0:
      ind = self.queue.pop()
      result = 0 
      for i in range(0, 500000):
        if i % ind == 0:
          result = result + 1
      self.results.append(result)
      calcs = calcs + 1

if __name__=="__main__":
  ts = time.time()
  q = list(range(10, 70))
  print(q)
  c = CalcQueue(q)
  #c.calc_last()
  threads = []
  num_threads = 20
  for i in range(num_threads):
    t = threading.Thread(target=c.calc_last)
    t.start()
    threads.append(t)
  for t in threads:
    t.join()
  ts2 = time.time()
  c.results.sort()
  print("Results = {}".format(c.results))
  print("Time elapsed = {}".format(ts2-ts))
