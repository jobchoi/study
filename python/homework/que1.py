# 함수 선언
def isQueueFull():
    global SIZE, queue, front, rear
    # 원형 큐에서 큐가 가득 찬 상태를 확인
    if (rear + 1) % SIZE == front:
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    # 큐가 비어있는 상태를 확인
    if front == rear:
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print("큐가 꽉 찼습니다")
        return
    rear = (rear + 1) % SIZE  # rear를 한 칸 이동
    queue[rear] = data  # 데이터 추가

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print("큐가 비었습니다.")
        return None
    front = (front + 1) % SIZE  # front를 한 칸 이동
    data = queue[front]  # 데이터를 가져옴
    queue[front] = None  # 데이터 제거
    return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print("큐가 비었습니다.")
        return None
    # 큐에서 가장 앞에 있는 데이터를 확인
    return queue[(front + 1) % SIZE]

def calcTime():
    global SIZE, queue, front, rear
    timeSum = 0  # 초기 합계는 0
    cntNum = (front + 1) % SIZE  # front 다음 위치부터 시작

    # 큐의 모든 요소를 순회하면서 시간
