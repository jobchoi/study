
# # 함수명 : calculateSum
# # 파라미터 : intNum_list
# # 리턴(결과 반환) :  
# def calculateSum(intNum_list):
#     resultSum = 0

#     for num in intNum_list:
#         resultSum += num
#     return resultSum


# # 예시 정수 리스트
# example_list = [1,2,3,4,5]

# # 함수 호출 -> 합계산
# resultSum = calculateSum(example_list)

# # 결과 출력
# print(f"리스트 {example_list}의 합 : {resultSum}")


# STUDENT = 3

# def getScoData():
#     getIntScores = []
    
#     # 다른 조건없이 반복횟수만 주고 싶을 때  '_'은 관례적인 변수
#     for _ in range(STUDENT):
#         getIntScores.append(int(input("성적입력 : ")))                

#     return getIntScores


# def avgCal(getScoList):
#     resultAvg = 0

#     # C와는 다르게 인덱스가 아닌 값을 가지고 반복문 연산을 수행
#     # buf(변수명은 사용자가 알아서) 변수에 파라미터 값을 꺼내 저장
#     for buf in getScoList:  
        
#         # 파라미터(여기서는 list)에서 꺼낸 값을 저장한 변수를 가지고, 리턴 변수에 누적합을 수행
#         resultAvg += buf    
    
#     resultAvg = resultAvg / STUDENT
    
#     return resultAvg

# resultScores = avgCal(getScoData())

# print(f"Result : {resultScores}")



# =================== 메서드 오버라이딩을 해서 list에 입력받아보기 ===================
# # 클래스
# class Animal():
# # 이름을 입력받는 함수생성
#     def getName(self):
#         animalName = input("이름을 입력해주세요 : ")
        
#         # print(f"animalName : {animalName}")        
#         return animalName

# # 메서드 오버라이딩 연습하기
# class dogs(Animal): # Animal 클래스 상속

#     CNT = 3

#     def getName(self):
#         namelist = []

#         for _ in range(self.CNT):
#             namelist.append( super().getName()) # super().getName() -> Animal에 getName()

#         print(f"dogs Name : {namelist}")

# # 입력이 1번만 실행 -> 반복문x, list x
# ani1 = Animal()
# ani1.getName()

# # list를 만들어 for를 이용하여 list에 값을 입력받음
# # ani2 = dogs()
# # ani2.getName()


# # =================== 리스트 요소 찾기 ===================

# heroes = ["스파이더맨", "슈퍼맨", "헐크", "아이언맨", "배트맨"]
# index = heroes.index("아이언맨")


# if "슈퍼맨" in heroes:  # in을 통해 리스트내 요소가 있는지 if문에서 확인 할 수 있다
#     # .index() 를 통해 있는 요소라면 해당 인덱스를 찾을 수 있다
#     index = heroes.index("스파이더맨")
#     print(f"index : {index}")

# # =================== 리스트 요소 제거 ===================

# heroes = ["스파이더맨", "슈퍼맨", "헐크", "아이언맨", "배트맨"]
# heroes.pop(3)

# print(heroes)

# # =================== 리스트 중복요소 갯수 ===================
# my_list=[1, 7, 2, 7, 3, 7, 4, 5, 7]
# cntNum = my_list.count(7)

# print(f"중복숫자 갯수 : {cntNum}")