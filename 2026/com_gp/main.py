import inspect

def my_fun():
    caller_frame = inspect.currentframe().f_back # type: ignore
    line_no = caller_frame.f_lineno # type: ignore

    print("my_fun 실행중 ")

    print(f"함수 종료 후 돌아갈 번호 : {line_no}")



print("A(Line 11)")
print("A(Line 12)")
print("A(Line 13)")
print("my_fun 실행전 ")
my_fun()
print("my_fun 실행후 ")
print("B(Line 13)")