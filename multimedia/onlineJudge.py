# 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성

# 엔터를 구분으로 map 없이 코드를 구현한것은 에러는 없지만, 채점시 한줄에 스페이스바로 구분하여서 map으로 수정함
numA,numb  = map(int,(input().split()))


print((float)(numA / numb))
