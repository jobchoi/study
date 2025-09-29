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
RADIUS = 100
EXIT_POS = (0, -100)
DIRECTIONS = [0, 90, 180, 270]
STEP_NORMAL = 20
STEP_REDUCED = 10
BACK_OPTIONS = [5, 10, 15]

# 경계 원 그리기
def draw_boundary():
    b = turtle.Turtle()
    b.hideturtle()
    b.penup()
    b.goto(0, -RADIUS)
    b.pendown()
    b.circle(RADIUS)

# 출구 표시 (크게!)
def draw_exit():
    e = turtle.Turtle()
    e.hideturtle()
    e.penup()
    e.goto(EXIT_POS)
    e.dot(20, "red")  # 출구 크게 표시

# 경계 밖인지 확인
def is_out_of_bounds(x, y):
    return math.sqrt(x**2 + y**2) > RADIUS

# 출구 도착 확인 (반지름 15 이내면 도착으로 간주)
def reached_exit(x, y):
    return math.sqrt((x - EXIT_POS[0])**2 + (y - EXIT_POS[1])**2) < 15

# 후진 함수
def backtrack(stack):
    steps = min(random.choice(BACK_OPTIONS), len(stack))
    t.penup()
    for _ in range(steps):
        if stack:
            x, y = stack.pop()
            t.goto(x, y)
    t.pendown()

# 위치 반올림 (10 단위로 격자 정리)
def round_position(pos):
    return (round(pos[0]), round(pos[1]))

# 최단 경로 다시 그리기
def draw_optimal_path(path):
    t.clear()
    t.penup()
    t.color("blue")
    t.goto(path[0])
    t.pendown()
    t.speed(1)
    for pos in path[1:]:
        t.goto(pos)
    print("✅ 탈출 경로 그리기 완료")

# 이동 시도 함수
def try_move(step_size, visited):
    directions = DIRECTIONS[:]
    random.shuffle(directions)

    for direction in directions:
        t.setheading(direction)
        current_pos = t.position()

        # 예측 이동 위치
        t.forward(step_size)
        new_pos = round_position(t.position())
        t.goto(current_pos)  # 원위치로 복귀

        if new_pos not in visited and not is_out_of_bounds(*new_pos):
            t.setheading(direction)
            t.forward(step_size)
            return True
    return False

# 초기 화면
draw_boundary()
draw_exit()
t.penup()
t.goto(0, 0)
t.pendown()

# 상태 변수
path_stack = []
visited = set()
step_size = STEP_NORMAL

# 탐색 루프
while True:
    curr_pos = round_position(t.position())
    path_stack.append(t.position())
    visited.add(curr_pos)

    moved = try_move(step_size, visited)

    if not moved:
        print("❌ 막다른 길... 후진 중")
        backtrack(path_stack)
        step_size = STEP_REDUCED
        continue

    if reached_exit(*t.position()):
        print("🎯 출구 도착!")
        break

# 최적 경로 다시 그리기
draw_optimal_path(path_stack)
turtle.done()
