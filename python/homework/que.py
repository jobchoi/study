## 함수 선언 부분##
def isQueueFull():
    global SIZE, queue, front, rear
    if(rear==SIZE-1):
        return True
    else:
        return False

def isQueunEmpty():
    global SIZE, queue, front, rear
    if (front==rear):
        return True
    else:
        return False
def enQueue(data):  #입력
    global SIZE, queue, front, rear
    if(isQueueFull()):   #만약꽉찼으면 메시지 출력후 리턴
        print("큐가 꽉 찼습니다")
        return
    rear +=1 #꼬리를 한칸뒤로 하고
    queue[rear]=data #데이터 입력

def deQueue():   # 출력
    global SIZE, queue, front, rear
    if (isQueunEmpty()):   #만약 비어있으면 메시지 출력
        print("큐가 비었습니다")
        return None
    front +=1 #머리 한칸뒤로 하고
    data=queue[front] #머리에서 데이터를 가져온다
    queue[front]=None  #나온 자리는 None 로 비워둔다

    for i in range(front+1,rear+1) :
        queue[i-1]=queue[i]
        queue[i]=None
    front =-1  #값 입력저장
    rear -=1   #rear값에 -1을하고 저장

    return data
def peek():  #
    global  SIZE, queue, front, rear
    if(isQueueEmpty()):
        print("큐가 비었습니다")
        return None
    return queue[front+1]

##전역 변수 선언 부분#
SIZE=5
queue=[None for _ in range(SIZE)]
front= rear=-1
## 메인 코드 부분
if __name__=="__main__":
    enQueue("정국")
    print("정국이 들어간 후, 대기줄 상태 :",queue)

    enQueue("뷔")
    print("\n뷔가 들어간 후\n대기줄 상태 :",queue)

    enQueue("지민")
    print("\n지민이 들어간 후\n대기줄 상태 :",queue)

    enQueue("진")
    print("\n진이 들어간 후\n대기줄 상태 :",queue)

    enQueue("슈가")
    print("\n슈가가 들어간 후\n대기 줄 상태 : ",queue)

    print("==================== EnQue End ====================");
    for _ in range(rear+1):
        print(deQueue(),'님 식당에 들어감') #나오는 손님이름
        print("대기줄 상태 :",queue)
    print("식당 영업종료!")
