import threading
import sys

a = 1
b = 2
lock = threading.Lock()

def fibo(name):
    global a, b

    lock.acquire() # lock +
    print("[Thread", name + "] : ", a)
    a, b = b, a + b
    lock.release() # lock -

if __name__ == '__main__':
    threads = []

    for _ in range(5):
        t1 = threading.Thread(target=fibo, args=("1"))
        t2 = threading.Thread(target=fibo, args=("2"))

        t1.start()
        t2.start()