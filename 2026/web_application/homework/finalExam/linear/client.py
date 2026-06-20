import sys
import os
from tkinter import *
from socket import *

PORT = 2500
BUFSIZE = 1024

class MLClient:
    def __init__(self):
        self.slope = 0.0
        self.intercept = 0.0
        self.raw_x = []
        self.raw_y = []
        
        # 소켓 초기화 및 서버 연결
        self.sock = socket(AF_INET, SOCK_STREAM)
        try:
            self.sock.connect(('localhost', PORT))
        except:
            print("Error: Start the Server first!")
            sys.exit()
            
        self.init_gui()
        
    def init_gui(self):
        self.root = Tk()
        self.root.title("Linear Regression Predictor")
        
        # 1구역: 파일 전송 및 학습
        self.lbl_file = Label(self.root, text="Step 1: Send CSV File to Server", font=("Verdana", 11, "bold"))
        self.lbl_file.grid(row=0, column=0, columnspan=2, pady=5)
        
        self.btn_train = Button(self.root, text="Send CSV & Train Model", bg="#3b82f6", fg="black", font=("Verdana", 10), command=self.send_csv_file)
        self.btn_train.grid(row=1, column=0, columnspan=2, ipady=3, sticky=E+W, padx=10)
        
        # 모델 상태 표시 레이블
        self.lbl_model = Label(self.root, text="Model Status: Untrained", fg="orange", font=("Verdana", 10))
        self.lbl_model.grid(row=2, column=0, columnspan=2, pady=5)
        
        # 2구역: 새로운 데이터로 결과 예측
        self.lbl_predict = Label(self.root, text="Step 2: Predict New Y Value", font=("Verdana", 11, "bold"))
        self.lbl_predict.grid(row=3, column=0, columnspan=2, pady=5)
        
        self.lbl_x = Label(self.root, text="New X Input:")
        self.entry_x = Entry(self.root, width=10)
        self.lbl_x.grid(row=4, column=0, sticky=E, padx=5)
        self.entry_x.grid(row=4, column=1, sticky=W, padx=5)
        
        self.btn_pred = Button(self.root, text="Get Predict Result (Y)", bg="#10b981", fg="black", font=("Verdana", 10), command=self.predict_y)
        self.btn_pred.grid(row=5, column=0, columnspan=2, ipady=3, sticky=E+W, padx=10, pady=5)
        
        self.lbl_result = Label(self.root, text="Predicted Y: -", font=("Verdana", 12, "bold"), fg="blue")
        self.lbl_result.grid(row=6, column=0, columnspan=2, pady=5)

        # 3구역: [기능 추가] 자체 그래픽 차트를 그릴 도화지(Canvas) 위젯 배치
        self.canvas = Canvas(self.root, width=360, height=220, bg="white", bd=1, relief=SUNKEN)
        self.canvas.grid(row=7, column=0, columnspan=2, padx=15, pady=10)

    def send_csv_file(self):
        ''' CSV 데이터 파일을 읽어서 서버로 전송하는 함수 '''
        try:
            # 절대 경로 자동 계산 로직
            current_dir = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(current_dir, "students2025.csv")
            
            with open(csv_path, "r", encoding="utf-8") as f:
                csv_data = f.read()
                
            # 원시 데이터를 가공하여 로컬 리스트에 보관
            self.raw_x.clear()
            self.raw_y.clear()
            for line in csv_data.split('\n'):
                if not line.strip() or line.lower().startswith('x'):
                    continue
                try:
                    px, py = line.split(',')
                    self.raw_x.append(float(px))
                    self.raw_y.append(float(py))
                except:
                    continue
                
            # 서버로 파일 스트림 인코딩 전송
            self.sock.sendall(csv_data.encode('utf-8'))
            
            # 서버가 연산한 학습 결과 수신
            res = self.sock.recv(BUFSIZE).decode('utf-8')
            
            if "Error" in res:
                self.lbl_model.config(text="Train Failed: Data Error", fg="red")
                return
                
            self.slope, self.intercept = map(float, res.split(','))
            self.lbl_model.config(text=f"Success! W:{self.slope:.2f} / b:{self.intercept:.2f}", fg="lightgreen")
            print(f"==> Model Trained. Slope: {self.slope:.4f}, Intercept: {self.intercept:.4f}")
            
            # [호출] 수신 성공 시 캔버스에 즉시 깔끔한 그래픽 차트 렌더링
            self.draw_canvas_graph()
            
        except FileNotFoundError:
            self.lbl_model.config(text="Error: 'students2025.csv' not found.", fg="red")
        except Exception as e:
            self.lbl_model.config(text=f"Network Error: {e}", fg="red")

    def predict_y(self):
        ''' 학습된 파라미터로 결과를 연산하는 함수 '''
        try:
            x_val = float(self.entry_x.get().strip())
            y_val = (self.slope * x_val) + self.intercept
            self.lbl_result.config(text=f"Predicted Y: {y_val:.2f}")
        except ValueError:
            self.lbl_result.config(text="Error: Input must be numeric!")

    def draw_canvas_graph(self):
        ''' 외부 라이브러리 없이 GUI 도화지(Canvas)에 2차원 회귀분석 그래프를 그리는 함수 '''
        if not self.raw_x:
            return
            
        # 기존에 그려진 요소들 싹 비우기
        self.canvas.delete("all")
        
        # 캔버스 크기 및 안전 마진 설정
        c_width = 360
        c_height = 220
        margin = 30
        
        # 데이터의 경계값 산출
        min_x, max_x = min(self.raw_x), max(self.raw_x)
        min_y, max_y = min(self.raw_y), max(self.raw_y)
        
        # 데이터 좌표를 캔버스 픽셀 좌표로 변환해주는 내부 헬퍼 람다 식
        def get_cx(x):
            return margin + (x - min_x) / (max_x - min_x + 1e-9) * (c_width - 2 * margin)
        def get_cy(y):
            return c_height - margin - (y - min_y) / (max_y - min_y + 1e-9) * (c_height - 2 * margin)
            
        # 1. 옅은 회색으로 격자 가이드 축 그리기
        self.canvas.create_line(margin, c_height - margin, c_width - margin, c_height - margin, fill="#cbd5e1", width=2)
        self.canvas.create_line(margin, margin, margin, c_height - margin, fill="#cbd5e1", width=2)
        
        # 2. 실제 데이터 분포를 파란색 작은 원(Scatter Plot)들로 배치
        for i in range(len(self.raw_x)):
            cx = get_cx(self.raw_x[i])
            cy = get_cy(self.raw_y[i])
            # 반지름 3짜리 데이터 포인트 생성
            self.canvas.create_oval(cx-3, cy-3, cx+3, cy+3, fill="#3b82f6", outline="#1e3a8a")
            
        # 3. 모델이 수립한 회귀 직선을 붉은색 강한 선(Regression Line)으로 플로팅
        start_x = min_x
        end_x = max_x
        start_y = (self.slope * start_x) + self.intercept
        end_y = (self.slope * end_x) + self.intercept
        
        self.canvas.create_line(get_cx(start_x), get_cy(start_y), get_cx(end_x), get_cy(end_y), fill="#ef4444", width=3)
        print("==> GUI Canvas Chart Rendering Completed.")

if __name__ == "__main__":
    client = MLClient()
    mainloop()