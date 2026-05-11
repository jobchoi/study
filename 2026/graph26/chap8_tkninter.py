from tkinter import *

# # 1. 객체 생성
# root = Tk()
# btn = Button(root, text="This is a button!")
# btn.pack()

# print("=== 1. 객체 고유 메모리 주소 (id) ===")
# root_id = id(root)
# btn_id = id(btn)
# print(f"root (스케치북) 의 주소 : {root_id}")
# print(f"btn  (스티커)   의 주소 : {btn_id}")
# print("-" * 40)

# print("=== 2. 자식 -> 부모 역추적 (Child to Parent) ===")
# # 위젯의 '.master' 속성은 자신의 부모 객체를 가리킵니다.
# parent_of_btn = btn.master
# print(f"btn이 기억하는 부모의 주소 : {id(parent_of_btn)}")
# print(f"결과: btn.master의 주소가 root의 주소와 같습니까? -> {id(parent_of_btn) == root_id}")
# print("-" * 40)

# print("=== 3. 부모 -> 자식 탐색 (Parent to Children) ===")
# # '.winfo_children()' 메서드는 자신이 품고 있는 자식 객체들의 리스트를 반환합니다.
# children_of_root = root.winfo_children()
# first_child = children_of_root[0] # 첫 번째 자식 객체
# print(f"root가 가진 첫 번째 자식의 주소 : {id(first_child)}")
# print(f"결과: root의 첫 번째 자식 주소가 btn의 주소와 같습니까? -> {id(first_child) == btn_id}")

# root.mainloop()


# a = 10
# b = 20

# print(f"a값 : {a}\tid(a) : {id(a)}") 
# print("-" * 40)
# print(f"b값 : {b}\tid(b) : {id(b)}") 

# b = a
# print("-" * 40)
# print(f"a값 : {a}\tid(a) : {id(a)}") 
# print(f"b값 : {b}\tid(b) : {id(b)}") 

# print("Test start : b=a")
# print(f"case 1. - value b : {b}")

# print("-" * 40)

# a -= 20
# print(f"case 2. - a - 20 연산 후 b : {b}")
# print(f"case 2. - a - 20 연산 후 a : {a}")

# b = b + 50
# print(f"case 3. - b -= 10 연산 후 a : {a}")


# print("-" * 40)
# a = a + 5  # 연산 수행 (새로운 객체 생성 및 이름표 이동)
# print(f"불변책에 연산 후 a의 값: {a}, id: {id(a)}") # id 값이 확실하게 달라집니다!


list_a = [10, 20, 30]
list_b = list_a  # 두 이름표를 같은 리스트 객체에 연결

print("=== Test start : list_b = list_a ===")
print(f"list_a 값 : {list_a} \t id(list_a) : {id(list_a)}")
print(f"list_b 값 : {list_b} \t id(list_b) : {id(list_b)}")
print("-" * 40)

# 핵심 연산: 새로운 리스트를 만드는 것이 아니라, 기존 리스트의 첫 번째 내용물만 변경!
list_a[0] = 99

print("case 1. - list_a[0] = 99 연산 후")
print(f"list_a 값 : {list_a} \t id(list_a) : {id(list_a)}")
print(f"list_b 값 : {list_b} \t id(list_b) : {id(list_b)}")