import time
from threading import Thread

def dormir(n, segundos):
    print("Thread ", n, " dormindo: ", segundos, " segundos")
    time.sleep(segundos)
    print("Thread ", n, " acordou!")

for i in range(10):
    t = Thread(target=dormir, args=(i+1, i,))
    t.start()
