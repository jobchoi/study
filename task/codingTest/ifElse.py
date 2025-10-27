nowTh = int(input("H : "))
nowTm = int(input("M : "))
cookingTimeM = int(input("ct : "))
trTimeHour = 0
trTimeMin = 0
nowTh = nowTh + trTimeHour
nowTm = nowTm + trTimeMin

# print(f"{nowTh} : {nowTm}")
print(f"완료시간 - H : {nowTh}")
print(f"완료시간 - M : {nowTm}")

if nowTm + cookingTimeM > 60 :
    trTimeHour = (int)(( nowTm + cookingTimeM )/ 60)
    trTimeMin = (int)(( nowTm + cookingTimeM ) % 60)


print(f"% 연산결과 : {trTimeMin}")

