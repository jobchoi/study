import sys
import cv2 as cv # cv 대신 cv2 명시 (일반적)
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt5.QtCore import QTimer # 비디오 끊김 없이 재생하기 위해 필요


class BeepSound(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('삑소리 내기 (Mac)')
        self.setGeometry(200, 200, 400, 150) # 창 크기 조절

        # 버튼 생성
        shortBeepButton = QPushButton('짧게 삑', self)
        longBeepButton = QPushButton('길게 삑', self)
        quitButton = QPushButton('나가기', self)

        self.label = QLabel('환영합니다', self)

        # [수정 중요] 버튼 위치가 겹치지 않게 옆으로(x좌표) 이동시켰습니다.
        shortBeepButton.setGeometry(10, 10, 100, 30)
        longBeepButton.setGeometry(120, 10, 100, 30) # 10 -> 120
        quitButton.setGeometry(230, 10, 100, 30)     # 10 -> 230
        
        self.label.setGeometry(10, 50, 380, 70)

        # 이벤트 연결 (오타 수정: shor -> short)
        shortBeepButton.clicked.connect(self.shortBeepFunction)
        longBeepButton.clicked.connect(self.longBeepFunction)
        quitButton.clicked.connect(self.quitFunction)

    def shortBeepFunction(self):
        self.label.setText('Mac 시스템 사운드 (Funk) 재생')
        # Mac 터미널 명령어로 소리 재생
        os.system('afplay /System/Library/Sounds/Funk.aiff')

    def longBeepFunction(self):
        self.label.setText('Mac 시스템 사운드 (Ping) 재생')
        # 다른 소리 재생
        os.system('afplay /System/Library/Sounds/Ping.aiff') 
    
    def quitFunction(self):
        self.close()


class Video(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('비디오에서 프레임 수집')
        self.setGeometry(200, 200, 500, 100)

        VideoButton = QPushButton('비디오 켜기', self)
        captureButton = QPushButton('프레임 잡기', self)
        saveButton = QPushButton('프레임 저장', self)
        quitButton = QPushButton('나가기', self)

        VideoButton.setGeometry(10, 10, 100, 30)
        captureButton.setGeometry(110, 10, 100, 30)
        saveButton.setGeometry(210, 10, 100, 30)
        quitButton.setGeometry(310, 10, 100, 30)

        VideoButton.clicked.connect(self.videoFunction)
        captureButton.clicked.connect(self.captureFunction)
        saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)
        
        # 카메라 관련 변수 초기화
        self.cap = None
        self.frame = None
        self.capturedFrame = None
        
        # 타이머 설정 (while True 대신 사용)
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateFrame)

    # --- 함수들을 __init__ 밖으로 꺼냈습니다 (들여쓰기 수정) ---

    def videoFunction(self):
        # Mac에서는 cv.CAP_DSHOW를 제거하고 그냥 0을 쓰거나 cv.CAP_AVFOUNDATION 사용
        self.cap = cv.VideoCapture(0) 
        
        if not self.cap.isOpened():
            print("카메라를 열 수 없습니다.")
            return

        # 타이머 시작 (33ms마다 updateFrame 실행 -> 약 30fps)
        self.timer.start(33)

    def updateFrame(self):
        # 타이머에 의해 반복 실행되는 함수
        if self.cap is None: return
        
        ret, self.frame = self.cap.read() # 오타 수정: self.capread() -> self.cap.read()
        
        if ret:
            cv.imshow('video display', self.frame)
        else:
            print("프레임을 읽을 수 없습니다.")

    def captureFunction(self):
        if self.frame is not None:
            self.capturedFrame = self.frame.copy() # 원본 보호를 위해 copy() 권장
            cv.imshow('Capture Frame', self.capturedFrame)
        else:
            print("비디오가 켜져있지 않습니다.")

    def saveFunction(self):
        if self.capturedFrame is not None:
            # Mac에서는 네이티브 파일 대화상자 문제로 options 추가 권장
            options = QFileDialog.Options()
            fname, _ = QFileDialog.getSaveFileName(self, 'save file', './', "Images (*.png *.jpg)", options=options)
            
            if fname: # 파일 이름을 지정했을 때만 저장
                cv.imwrite(fname, self.capturedFrame)
                print(f"저장 완료: {fname}")
        else:
            print("캡처된 프레임이 없습니다.")

    def quitFunction(self):
        self.timer.stop() # 타이머 정지
        if self.cap is not None:
            self.cap.release()
        cv.destroyAllWindows()
        self.close()


class Orim(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('오림')
        self.setGeometry(200, 200, 700, 200)

        fileButton = QPushButton('파일',self)
        paint

        
    def fileOpenFunction(self):
        fname, _ = QFileDialog.getSaveFileName(self, 'save file', './', "Images (*.png *.jpg)", options=options)
        self.img = cv.imread(fname[0])
        
        if self.img is None:
            sys.exit('파일을 저장할 수 없습니다')
        
        self.img_show=np.copy(self.img)
        cv.imshow('Painting',self.img_show)

        self.mask = np.zeros((self.img.shape[0], self.img.shape[1]), np.uint8)
        self.mask[:,:] = cv.GC_PR_BGD
    
    def paintFunction(self):
        cv.setMouseCallback('Painting',self.painting)
    
    def painting(self, event,x,y,flags,param):
        if event == cv.EVENT_LBUTTONDOWN:
            cv.circle(self.img_show(x,y), self.BrusgSiz,self.LColor, -1)
            cv.circle(self.mask, (x,y),self.BrushSiz, cv.GC_FGD, -1)
        elif event == cv.EVENT_RBUTTONDOWN:
            cv.circle(self.img_show(x,y), self.BrusgSiz,self.RColor, -1)
            cv.circle(self.mask, (x,y),self.BrushSiz, cv.GC_BGD, -1)
        
        elif event == cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
            cv.circle(self.img_show,(x,y),self.BrushSiz, self.RColor, -1)
            cv.circle(self.mask, (x,y), self.BrushSiz, cv.GC_BGD, -1)
        
        cv.imshow('Painting', self.img_show)
    
    def cutFunction(self):
        background = np.zeros((1,65), np.float64)
        foreground = np.zeros((1,65), np.float64)
        cv.grabCut(self.img, self.mask, None, background, foreground, 5, cv.GC_INIT_WITH_MASK)
        mask2 = np.where((self.mask==2) | (self.mask0),0,1).astype('uint8')
        self.grabImg = self.img * mask2[:,:,np.newaxis]
        cv.imshow('Scissoring',self.grabImg)

    def incFunction(self):
        self.BrushSiz = min(20,self.BrushSiz+1)

    def decFunction(self):
        self.BrushSiz = max(1, self.BrushSiz-1)

    def saveFunction(self):
        fname = QFileDialog.getSaveFileName(self, '파일 저장','./')
        cv.imwrite(fname[0], self.grabImg)

    def quitFunction(self):
        cv.destroyAllWindows()
        self.close()
    





if __name__ == '__main__':
    app = QApplication(sys.argv)
    # win = Video()
    win 
    win.show()
    sys.exit(app.exec_())