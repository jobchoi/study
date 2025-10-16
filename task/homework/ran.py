import random

intBuf100=[0]*100

for i in range(100):
    intBuf100[i]=random.randrange(0,100,1)

for i in range(100):
    formatted = str(intBuf100[i]).zfill(3)
    print(formatted,end="  ")
    # print(' ')
    if i % 10 == 9:
        print("\t")

