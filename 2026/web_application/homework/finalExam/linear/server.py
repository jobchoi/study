from socket import *

PORT = 2500
BUFSIZE = 8192 # CSV 파일 전체 내용을 한 번에 받아야 하므로 버퍼 크기를 넉넉하게 설정

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('', PORT))
s.listen(1)

print("Linear Regression Server is waiting...")
conn, addr = s.accept()
print(f"Connected by {addr}")

while True:
    try:
        # 클라이언트가 보낸 CSV 파일 텍스트 원문 수신
        data = conn.recv(BUFSIZE)
        if not data:
            break
            
        csv_text = data.decode('utf-8').strip()
        print("==> CSV 데이터를 수신했습니다. 학습을 시작합니다.")
        
        # CSV 파싱 로직 (첫 줄 헤더 제외하고 X, Y 추출)
        lines = csv_text.split('\n')
        X = []
        Y = []
        
        for line in lines:
            if not line.strip() or line.startswith('x') or line.startswith('X'): 
                continue # 헤더나 빈 줄 패스
            try:
                parts = line.split(',')
                X.append(float(parts[0]))
                Y.append(float(parts[1]))
            except:
                continue

        # 수식 기반 선형회귀 학습 알고리즘 (최소제곱법)
        if len(X) > 0:
            mean_x = sum(X) / len(X)
            mean_y = sum(Y) / len(Y)
            
            num = 0 # 분자
            den = 0 # 분모
            for i in range(len(X)):
                num += (X[i] - mean_x) * (Y[i] - mean_y)
                den += (X[i] - mean_x) ** 2
                
            slope = num / den              # 기울기 (a)
            intercept = mean_y - (slope * mean_x) # 절편 (b)
            
            print(f"학습 완료 -> 기울기(a): {slope:.4f}, 절편(b): {intercept:.4f}")
            
            # 클라이언트가 파싱하기 좋게 "기울기,절편" 형태로 묶어 전송
            response = f"{slope},{intercept}"
            conn.sendall(response.encode('utf-8'))
        else:
            conn.sendall("Error: No Data".encode('utf-8'))
            
    except Exception as e:
        print(f"오류 발생: {e}")
        break

conn.close()
s.close()