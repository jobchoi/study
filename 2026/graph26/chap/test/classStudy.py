# class Test1():
    
#     cnt = 0

#     def __init__(self):
#         print("Test1에 생성자")


# a = Test1()
# b = Test1()

# a.cnt = 1
# print(f"a val ==> {a.cnt} // id : {id(a.cnt)}")
# print(f"b val ==> {b.cnt} // id : {id(b.cnt)}")


class Test1():
    cnt = 0

    def __init__(self, cntTest):
        print(f"{self} - Test1에 생성자 (self)")
        self.cnt = cntTest
        print(f"생성자 :cntTest  {id(self.cntTest)}")  # 출력: {}
        print(f"value :cntTest  {(self.cntTest)}")  # 출력: {}

a = Test1(100)

# 1. 값을 변경하기 전 내부 들여다보기
print(f"변경 전 a: {id(a.cntTest)} , value : {a.cntTest}, {a.cntTest}")  # 출력: {}
a.cntTest = 1

# 2. 값을 변경한 후 내부 들여다보기 (🔥 핵심)
print("변경 전 a:", id(a.cntTest))  # 출력: {}
