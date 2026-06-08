# class BankAccount:
#     def __init__(self):
#         self.__balance = 0        

#         if self.__balance < 0:
#             print("출금액은 0원보다 낮아질 수 없습니다.")

#     def withdraw(self, amount):
#         self.__balance += amount
#         print("통장에",amount,"가 입금되었음")
#         print("현재 잔액 : ",self.__balance)
#         return self.__balance
#     def deposit(self, amount):
#         self.__balance -=amount
#         print("통장에",amount,"가 출금되었음")
#         print("현재 잔액 : ",self.__balance)

#         return self.__balance
    

# a = BankAccount()
# a.deposit(100)
# a.withdraw(10)



class BankAccount:
    def __init__(self):
        self.__balance = 0        

        if self.__balance < 0:
            print("출금액은 0원보다 낮아질 수 없습니다.")

    def withdraw(self, amount):
        self.__balance -= amount
        print("통장에",amount,"가 입금되었음")
        print("현재 잔액 : ",self.__balance)
        return self.__balance
    
    def deposit(self, amount):
        
        print("현재 잔액 : ",self.__balance)
        
        try:
            self.__balance +=amount
        
            if self.__balance <= 0:
                print("출금 가능한 금액이 부족합니다.")
                SystemError(-1)
                return -1
            else :
                print("통장에",amount,"가 출금되었음")
                print("현재 잔액 : ",self.__balance)
                return self.__balance
        except self.__balance as e:
            print("--1")


    

a = BankAccount()
a.deposit(100)
a.withdraw(10)
