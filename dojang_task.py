import sys


# ap=102
# print(ap*0.6+225)

# a=50
# b=100
# c=None
# print(a)
# print(b)
# print(c)

# 6.7 심사문제: 변수 만들기

# a,b,c,d = map(int,input().split())
# # print( (int)((a+b+c+d)/4) )
# print( ((a+b+c+d)//4) ) # 버림 연산을 함께 함

# print(16,9,end=':')
# print('Hello', '\n', 'Python', sep='')

# year, month, day, hour, minute, second = input().split()
# print(year, month, day, sep='-',end='T')
# print(hour, minute, second, sep=':')

# print( 8 is 4 * 2.0)

# print('''안녕하세요
#       파이썬입니다''')

# print("""안녕하세요
#       파이썬입니다""")

# print('Hello, \'Python\'')
# s="'Python' is a \"programming language\" \nthat lets you work quickly \nand \nintegrate systems more effectively."
# print(s)

'''
표준 입력으로 정수가 입력됩니다. range의 시작하는 숫자는 -10, 끝나는 숫자는 10이며 입력된 정수만큼 증가하는 숫자가 들어가도록 튜플을 만들고, 해당 튜플을 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).
'''

getNum = int(input())
tNum = tuple(range(-10,10,getNum))
print(tNum)