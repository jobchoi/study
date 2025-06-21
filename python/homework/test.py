import threading

x = 0

def increment1():
    global x
    x += 1

def increment2():
    global x
    x -= 1

def thread_task1(lock):
    for _ in range(100000):
        lock.acquire()
        increment1()
        lock.release()

def thread_task2(lock):
    for _ in range(100000):
        lock.acquire()
        increment2()
        lock.release()

def main_task():
    global x
    x = 0

    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task1, args=(lock,))
    t2 = threading.Thread(target=thread_task2, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i, x))