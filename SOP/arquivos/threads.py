#!/usr/bin/python

import threading
import time

def worker1():
    for i in range(10):
        print i
        time.sleep(0.5)

def worker2():
    for i in range(9, -1, -1):
        print i
        time.sleep(0.5)

t1 = threading.Thread(target=worker1)
t2 = threading.Thread(target=worker2)

t1.start()
while t1.isAlive():
    pass

t2.start()
