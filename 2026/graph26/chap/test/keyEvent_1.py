from tkinter import *

# 콜백 함수 정의    
def key_press(event):
    print("Key pressed:", event.keysym) 

root = Tk()
root.geometry("200x200")

# 키보드 이벤트 바인딩
# 바인딩 -> 이벤트가 발생했을 때 호출되는 함수를 연결
# 콜백함수 등록.
root.bind("<KeyPress>", key_press)
root.focus_set()

# 이벤트 루프 시작
root.mainloop()
