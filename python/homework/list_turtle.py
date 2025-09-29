import turtle
import random

# 🌟 Node 클래스 (RGB 값 저장)
class Node:
    def __init__(self, r, g, b):
        self.data = (r, g, b)  # RGB 값 저장
        self.next = None
        self.prev = None

# 🌟 LinkedList 클래스
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, r, g, b):
        """리스트 끝에 (R, G, B) 추가"""
        new_node = Node(r, g, b)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def to_list(self):
        """연결 리스트를 리스트로 변환"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def from_list(self, data_list):
        """정렬된 리스트를 다시 연결 리스트로 변환"""
        self.head = None
        self.tail = None
        self.size = 0
        for r, g, b in data_list:
            self.append(r, g, b)

    def sort(self):
        """RGB 값을 오름차순으로 정렬"""
        def rgb_to_int(r, g, b):
            """RGB를 하나의 값으로 변환 (R * 256^2 + G * 256 + B)"""
            return r * 256**2 + g * 256 + b

        # RGB 튜플을 하나의 값으로 변환한 뒤 정렬
        sorted_list = sorted(self.to_list(), key=lambda x: rgb_to_int(x[0], x[1], x[2]))
        self.from_list(sorted_list)  # 정렬된 리스트를 다시 연결 리스트로 변환

    def display(self):
        """리스트 출력"""
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        print("Sorted LinkedList:", result)

# 🐢 Turtle을 이용한 시각화 함수
def draw_circle(t, x, y, radius, color, text):
    """원형 노드를 그리는 함수"""
    t.penup()
    t.goto(x, y - radius)  # 원의 중심 보정
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # RGB 값 표시
    t.penup()
    t.goto(x, y - radius // 2)
    t.color("black")
    t.write(text, align="center", font=("Arial", 10, "bold"))
    t.pendown()

def draw_arrow(t, x1, y1, x2, y2):
    """화살표를 그리는 함수"""
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

# 🏗 연결 리스트 생성
linked_list = LinkedList()

# 10개의 랜덤 RGB 값 추가
for _ in range(10):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    linked_list.append(r, g, b)

print("Before Sorting:")
linked_list.display()

# 🚀 RGB 값을 오름차순으로 정렬
linked_list.sort()

print("After Sorting:")
linked_list.display()

# 🐢 Turtle 설정
screen = turtle.Screen()
screen.setup(width=900, height=400)
screen.bgcolor("white")
screen.tracer(0)  # 애니메이션 속도 향상을 위해

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# 🖌️ 정렬된 노드 그리기
current = linked_list.head
x, y = -350, 0  # 시작 좌표
radius = 30  # 원 반지름

while current:
    # RGB 값 적용
    color = (current.data[0] / 255, current.data[1] / 255, current.data[2] / 255)  # 0~1 범위로 정규화
    text = f"({current.data[0]}, {current.data[1]}, {current.data[2]})"  # 표시할 RGB 값

    # 원형 노드 그리기
    draw_circle(t, x, y, radius, color, text)

    # 다음 노드가 있다면 화살표 표시
    if current.next:
        draw_arrow(t, x + radius, y, x + 80 - radius, y)

    current = current.next
    x += 100  # 다음 노드 위치로 이동

# 🐢 화면 업데이트
screen.update()
turtle.done()
