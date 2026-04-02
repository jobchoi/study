import turtle
import sys

class myTutle():

    def __inin__(self):
        self.recLen = 0
        self.xPosition = 0
        self.yPosition = 0
        return

    # def chk_print(self):
    #     print("Hello Class")
    #     return

    def getRecSize(self, len):
        self.recLen = len

        return
    
    def defaultRecTutle(self ):

        for i in range(4):
            turtle.fd(self.recLen)
            turtle.left(90) 
        turtle.done()
        return    

    def winSize(self):
        s = turtle.Screen()
        print("=========================>")
        print(f"window Height : {s.window_height()}")
        print(f"window width : {s.window_width()}")
        return
    
    def setPosirion(self, xPosition, yPosition) :
        self.xPosition = xPosition
        self.yPosition = yPosition

        self.xPosition = int(input("get x position"))
        self.yPosition = int(input("get y position"))

        turtle.setpos(self.xPosition, self.yPosition)
        # 좌표를 입력 받고, int()식으로 형변환 하려는데, typeError를 주길래 찾아보는중
        print(f"==========> type - height : {type(turtle.window_height)}") # type : class-> function()
        # turtle.window_height # 좌표 값 형변환 작업중
        # print(f"==========> type - width: {turtle.window_width}")

        if xPosition >= 0 and yPosition >= 0:
            if xPosition >= turtle.window_height :
                yPosition = turtle.window_height
                xPosition = turtle.window_width

                self.defaultRecTutle()

        return

a = myTutle()

a.winSize()

a.setPosirion(100,40)
a.getRecSize(200)
