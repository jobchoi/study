# 사용자에게 정수 5개를 입력받고,
# 평균, 최댓값, 최솟값, 정렬 결과를 딕셔너리 형태로 반환하시오.
# ✨ 힌트

# 1. input() → 문자열이므로 int()로 변환해야 함
# 2. max(), min(), sum(), len()을 적극 활용
# 3. 결과는 딕셔너리로 구성


# listNums = [] # 글로벌에서 로컬로 변경

def analyze(nums):
    # print(f" max : {max(getListNum)}")
    # print(f" min : {min(getListNum)}")
    # print(f" sort : {sorted(getListNum)}")        

    # print(f"result : {getListNum}")    
    # pass
    if not nums:
        print("빈 목록입니다")
        return
    result = {
        "개수": len(nums),
        "평균": sum(nums)/len(nums),
        "최대값": max(nums),
        "최소값": min(nums),
        "오름차순": sorted(nums)        
    }

    print("\[결과]")
    for k, v in result.items():
        print(f"{k} : {v}")
    return result

# def get_number():
def get_number(prompt="숫자입력"):

    # inputNum = input(int("숫자 입력"))
    # # pass
    # return inputNum
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print("정수를 입력하세요")

# def main():
def main(n = 10):

    nums = []

    # for i in range(10):
    for i in range(n):
        # listNums.append(get_number())
        nums.append(get_number(f"{i+1}번째 숫자"))
    
    # analyze(listNums)
    analyze(nums)
    

if __name__ == "__main__":
    main()