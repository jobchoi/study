# 사용자에게 정수 5개를 입력받고,
# 평균, 최댓값, 최솟값, 정렬 결과를 딕셔너리 형태로 반환하시오.
# ✨ 힌트

# 1. input() → 문자열이므로 int()로 변환해야 함
# 2. max(), min(), sum(), len()을 적극 활용
# 3. 결과는 딕셔너리로 구성


listNums = []

def analyze(getListNum):
    print(f" max : {max(getListNum)}")
    print(f" min : {min(getListNum)}")
    print(f" sort : {sorted(getListNum)}")        

    print(f"result : {getListNum}")    
    pass

def get_number():
    inputNum = input(int("숫자 입력"))
    # pass
    return inputNum

def main():
    for i in range(10):
        listNums.append(get_number())
    analyze(listNums)
    

if __name__ == "__main__":
    main()