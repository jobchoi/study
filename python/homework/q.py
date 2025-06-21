class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        chk =(self.rear + 1) % self.size == self.front
        print("초기값확인 : ",chk)
        return chk

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full!")
            return
        if self.front == -1:  # 큐가 비어 있을 때
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(f"Enqueued: {data}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        removed_data = self.queue[self.front]
        if self.front == self.rear:  # 큐에 하나만 남아 있을 때
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Dequeued: {removed_data}")
        return removed_data

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        i = self.front
        print("Queue elements:", end=" ")
        while i != self.rear:
            print(self.queue[i], end=" ")
            i = (i + 1) % self.size
        print(self.queue[self.rear], end=" ")  # 마지막 요소 출력
        print()

# 원형 큐 사용 예시
cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)

cq.display()

cq.dequeue()
cq.enqueue(60)

cq.display()
