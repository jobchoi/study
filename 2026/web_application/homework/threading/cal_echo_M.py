
class CalEchoM:
    def __init_(self, data):
        self.data = data    
    def cal_task(self, spldata):
        if "+" in spldata:
            print("+ chk : OK")
            getData = spldata.split("+")
            print(f"{getData[0]} + {getData[1]} = {int(getData[0]) + int(getData[1])}")

            return int(getData[0]) + int(getData[1])
        elif "-" in spldata:
            print("- chk : OK")
            getData = spldata.split("-")
            print(f"{getData[0]} - {getData[1]} = {int(getData[0]) - int(getData[1])}")

            return int(getData[0]) - int(getData[1])
        elif "*" in spldata:
            print("* chk : OK")
            getData = spldata.split("*")
            print(f"{getData[0]} * {getData[1]} = {int(getData[0]) * int(getData[1])}")

            return int(getData[0]) * int(getData[1])
        elif "/" in spldata:
            print("/ chk : OK")
            getData = spldata.split("/")
            try:
                if int(getData[1]) == 0:
                    print("0으로 나눌 수 없습니다.")                
                else :
                    print(f"{getData[0]} / {getData[1]} = {int(getData[0]) / int(getData[1])}")
                    return int(getData[0]) / int(getData[1])
            except ValueError:
                print("입력 오류 - 숫자만 입력해주세요.")
                return
        else:
            print("입력 오류 - 연산자 오류")
    def chk_input(self, spldata):
        for i in spldata:
            if i not in ['+', '-', '*', '/','%'] and not i.isdigit():
                print("연산자 오류 - +, -, *, /, % 연산자만 입력해주세요.")
                return False
        return True




