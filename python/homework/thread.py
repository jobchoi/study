import threading

x = 0
lock = threading.Lock()

def increment1():
    global x
    x += 1

def increment2():
    global x
    x -= 1

def thread_task1():
    global x
    for _ in range(10):
        for _ in range(100):
            for _ in range(100):
                # lock.acquire()
                increment1()
                # lock.release()



def thread_task2():
    global x
    for _ in range(10):
        for _ in range(100):
            for _ in range(100):
                # lock.acquire()
                increment2()
                # lock.release()

def main_task():
    global x
    x = 0


if __name__ == "__main__":
    
    main_task()
    flag=0

    # 스레드 락을 제거하여 race condition을 발생시킴
    t1 = threading.Thread(target=thread_task1)
    t2 = threading.Thread(target=thread_task2)

    t1.start()
    t2.start()

    for i in range(10):
        print("Iteration {0}: x = {1}".format(i, x))

    while True:
        flag += 1
       
        if x <= 0:
            print(f"Iteration ===============> {flag} : x = {x}")  # f-string을 사용하여 출력
            break

    t1.join()
    t2.join()
    



