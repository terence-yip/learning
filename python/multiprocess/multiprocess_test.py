#!/usr/local/bin/python3

import pprint
import time
import multiprocessing.pool

class CalcQueue:
  def __init__(self, queue):
    self.queue = queue
    self.results = {}
    self.num = 0

  def calc_last(self, item):
    result = 0
    for i in range(0, 500000):
      if i % item == 0:
        result = result + 1
    return result

if __name__=="__main__":
  ts = time.time()
  q = list(range(10, 70))
  print(q)
  c = CalcQueue(q)
  #c.calc_last()
  threads = []
  num_threads = 2
  with multiprocessing.pool.Pool(num_threads) as p:
    c.results = p.map(c.calc_last, c.queue)
  ts2 = time.time()
  c.results.sort()
  print("Results = {}".format(c.results))
  print("Time elapsed = {}".format(ts2-ts))
