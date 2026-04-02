import pandas as pd
import qrcode
import os

# 결과 저장 폴더
output_dir = "qr_output"
os.makedirs(output_dir, exist_ok=True)

print("현재 경로:", os.getcwd())

# 엑셀 읽기
df = pd.read_excel("data.xlsx")

for i, row in df.iterrows():
    sn = str(row['S/N'])
    name = str(row['이름'])
    
    # QR에 들어갈 내용
    data = f"S/N: {sn}\n이름: {name}"
    
    # QR 생성
    qr = qrcode.make(data)
    
    # 파일명
    filename = f"{name}_{sn}.png"
    filepath = os.path.join(output_dir, filename)
    
    # 저장
    qr.save(filepath)

print("✅ QR 생성 완료! (qr_output 폴더 확인)") 


