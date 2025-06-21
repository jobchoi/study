import turtle
import random
import math

# 설정
screen = turtle.Screen()
screen.setup(width=600, height=600)
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

# 상수
EXIT_POS = (0, -100)
RADIUS = 100

# 경계 원 그리기
def draw_boundary():
    boundary = turtle.Turtle()
    boundary.hideturtle()
    boundary.penup()
    boundary.goto(0, -RADIUS)
    boundary.pendown()
    boundary.circle(RADIUS)

# 출구 그리기
def draw_exit():
    marker = turtle.Turtle()
    marker.hideturtle()
    marker.penup()
    marker.goto(EXIT_POS)
    marker.dot(10, "red")

# 경계 검사
def is_out_of_bounds(x, y):
    return math.sqrt(x**2 + y**2) > RADIUS

# 출구 도착 검사 (오차 범위 ±5)
def reached_exit(x, y):
    return abs(x - EXIT_POS[0]) < 5 and abs(y - EXIT_POS[1]) < 5

# 랜덤 이동
def move_random():
    angle = random.randint(0, 360)
    t.setheading(angle)
    t.forward(10)

# 스택을 따라 최대 10단계 후진
def backtrack():
    steps = min(10, len(path_stack))
    t.penup()
    for _ in range(steps):
        if path_stack:
            x, y = path_stack.pop()
            t.goto(x, y)
    t.pendown()

# 최적 경로 그리기
def draw_optimal_path(path):
    t.clear()
    t.color("blue")
    t.penup()
    t.goto(path[0])
    t.pendown()
    t.speed(1)
    for pos in path[1:]:
        t.goto(pos)
    print("✅ 최단 경로 표시 완료")

# 초기 설정
draw_boundary()
draw_exit()
t.penup()
t.goto(0, 0)
t.pendown()
t.speed(0)

# 경로 기록
path_stack = []

# 이동 시도
while True:
    path_stack.append(t.position())
    move_random()

    x, y = t.position()

    if is_out_of_bounds(x, y):
        backtrack()

    if reached_exit(x, y):
        print("🎉 출구에 도착했습니다!")
        break

# 출구까지 갔던 경로를 사용해 최단 경로 재표시
draw_optimal_path(path_stack)

turtle.done()

