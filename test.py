
# 날짜 입력 받기
n = int(input())

# 8월 1일이 화요일(Tue)이므로 기준일을 화요일로 설정

# a도 변수임, 변수는 값이 수시로 변할 수 있음.
a = 1

# a는 변수이므로 (a + n - 1) % 7 연산 후 결과값을 저장할 수 있음 
# 처음 a=1 -> a=연산결과 값
a = (a + n - 1) % 7 

# 요일 출력
if a == 1:
    print("Tue")
elif a == 2: #elif -> c,java등 다른 언어에 경우 else if로 표현 
    # else if, if조건이 충족 되지 않았을 때 체크, 만약 else if에서도 없다면
    # else문을 실행
    print( "Wed" )
elif a == 3:
    print("Thu")
elif a == 4:
    print( "Fri" )
elif a==5 :
    print("Sat")
elif a == 6:
    print("Sun")
elif a==0 :# a가 7(a==7)일 경우 % 연산자에 의해 0으로 떨어짐, 그래서 7이 아니라 0으로 값을 확인하여야 함
    print("Mon")