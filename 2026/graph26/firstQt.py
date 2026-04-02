from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QApplication
import sys
import os
from PyQt5.QtMultimedia import QSound 
#import winsound

class BeepSound(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle('삑 소리 내기') 		# 윈도우 이름과 위치 지정
        self.setGeometry(200,200,500,100)

        shortBeepButton=QPushButton('짧게 삑',self)	# 버튼 생성
        longBeepButton=QPushButton('길게 삑',self)
        quitButton=QPushButton('나가기',self)
        self.label=QLabel('환영합니다!',self)
        
        shortBeepButton.setGeometry(10,10,100,30)	# 버튼 위치와 크기 지정
        longBeepButton.setGeometry(110,10,100,30)
        quitButton.setGeometry(210,10,100,30)
        self.label.setGeometry(10,40,500,70)
        
        shortBeepButton.clicked.connect(self.shortBeepFunction) # 콜백 함수 지정
        longBeepButton.clicked.connect(self.longBeepFunction)         
        quitButton.clicked.connect(self.quitFunction)
       
    def shortBeepFunction(self):
        self.label.setText('주파수 1000으로 0.5초 동안 삑 소리를 냅니다.')   
        #winsound.Beep(1000,500)
        # QApplication.beep()
    
        # QSound.play('/Users/magasa/code/sound/1.beep.mp3')
        # QApplication.beep()
        self.play_short_beep()
        
    def longBeepFunction(self):
        self.label.setText('주파수 1000으로 3초 동안 삑 소리를 냅니다.')        
        #winsound.Beep(1000,3000) 
        #QSound.play('/Users/magasa/code/sound/1.beep.mp3')
        # QApplication.beep()
        self.play_long_beep()
                
    def quitFunction(self):
        self.close()

    def play_short_beep(self):
        # 1000Hz 주파수로 0.2초(짧게) 소리 발생
        # os.system('play -nq -t alsa synth 0.2 sine 1000 &')
        # os.system('PADSP_OUTPUT_CLASS=1 padsp play -nq synth 0.2 sine 1000 &')
        os.system('play -nq synth 0.1 sine 1000 &')

    def play_long_beep(self):
        # 1000Hz 주파수로 1.0초(길게) 소리 발생
        # os.system('play -nq -t alsa synth 1.0 sine 1000 &')
        os.system('play -nq synth 0.2 sine 500 &')
        
                
app=QApplication(sys.argv) 
win=BeepSound() 
win.show()
app.exec_()