from tkinter import *
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)

def print_fields():
    # 입력된 id와 pwd를 출력하는 함수
    print("id : %s\npwd : %s"%(e1.get(),e2.get()))

# Tkinter 윈도우 생성
root = Tk()

# 라벨과 입력 필드 생성 및 배치
Label(root, text="id").grid(row=0)
Label(root, text="pwd").grid(row=1)

# id와 pwd를 입력받는 Entry 위젯 생성
e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)    

# Submit 버튼과 Quit 버튼 생성 및 배치
Button(root, text="Submit", command=print_fields).grid(row=2, column=1,sticky=W, pady=4)
Button(root, text="Quit", command=root.quit).grid(row=3, column=1, sticky=W, pady=4)

print("=====> root.__dict__ <=====")
pp.pprint(root.__dict__)

print("=====> root.Tk <=====")
pp.pprint(dir(Tk))
# 이벤트 루프 시작
root.mainloop()