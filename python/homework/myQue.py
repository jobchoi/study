class myQueue:
    def __init__(self, size):
        self.size = size;
        self.queue = [None] * size;
        self.front = -1;
        self.rear = -1;
    
    def is_empty(self):
        return self.front == -1;

    def is_full(self):
        return (self.rear + 1) % self.size == self.front;

    def enqueue(self, data):
        if self.is_full():
            print("Queue is Full")
            return ;

        if self.front == -1:
            self.front = 0;
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data;

        print(f"Enqueueed : {data}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return ;
        removed_data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Dequeued : {removed_data}")
        return removed_data
    
    def peek(self):
        if self.is_empty():
            print("Queue is Empty!");
            return ;
        return self.queue[self.front]
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return 

        i=self.front
        print("Queue Elements : ",end=" ")
        while i != self.rear:
            print(self.queue[i], end=" ")
            i =(i+1)%self.size
        print(self.queue[self.rear],end=" ")
        print()


cq = myQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
print(" =============== chk 60 ===============")

cq.enqueue(60)

cq.display()

print(" =============== dequeue ===============")
cq.dequeue()
cq.display()

cq.enqueue(60)

cq.display()

