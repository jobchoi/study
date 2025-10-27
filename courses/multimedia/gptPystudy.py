# aster_stats_io.py
# 데이터 타입을 명시하는데 사용, 3.5버전부터 도입된 사항
from __future__ import annotations

# json 확장자 파일로 저장하기 위해 추가
import json
# csv 확장자 파일로 저장하기 위해 추가
import csv  

# 파라미터 타입 line, 문자열 입력을 -> list형식에 정수 타입으로 변경
def get_numbers_from_line(line: str) -> list[int]:
    
    # split()를 통해 공백 구분자로 들어온 입력을 자름
    """공백으로 구분된 정수 한 줄을 파싱"""
    parts = line.strip().split()
    return [int(p) for p in parts]

def summarize(nums: list[int]) -> dict:
    
    # 데이터 존재 여부 확인
    if not nums:
        # 없으면 메시지 출력 
        raise ValueError("빈 입력입니다.")
    # 딕셔너리 형태로 내장함수를 이용하여 결과값 저장
    return {
        "count": len(nums),
        "mean": sum(nums) / len(nums),
        "max": max(nums),
        "min": min(nums),
        "sorted": sorted(nums),
    }

# ---------- CSV ----------
def save_csv(stats: dict, path: str = "result.csv") -> None:
    """단일 통계 dict를 1행 CSV로 저장"""
    # 리스트(예: sorted)는 문자열로 저장(단순성 우선)
    row = {
        "count": stats["count"],
        "mean": stats["mean"],
        "max": stats["max"],
        "min": stats["min"],
        "sorted": " ".join(map(str, stats["sorted"])),
    }

    # 파일을 w(쓰기 모드)로 연다, 인코딩은 utf-8, 파일디스크립터(?) f에 저장
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        writer.writeheader()
        writer.writerow(row)

def load_csv(path: str = "result.csv") -> dict:

    # 파일을 읽기 모드로 연다.
    with open(path, "r", encoding="utf-8") as f:
        # 
        reader = csv.DictReader(f)

        row = next(reader)
    # 문자열을 원래 타입으로 복원
    stats = {
        "count": int(row["count"]),
        "mean": float(row["mean"]),
        "max": int(row["max"]),
        "min": int(row["min"]),
        "sorted": list(map(int, row["sorted"].split())),
    }
    return stats

# ---------- JSON ----------
def save_json(stats: dict, path: str = "result.json") -> None:
    """JSON은 구조를 그대로 보존(리스트도 그대로)"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, separators=(",", ":"))

def load_json(path: str = "result.json") -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# ---------- CLI 흐름 ----------
def main():
    line = input("정수들을 공백으로 입력하세요 (예: 5 1 6 10 80 ...):\n> ")
    nums = get_numbers_from_line(line)
    stats = summarize(nums)

    # 저장
    save_csv(stats, "result.csv")
    save_json(stats, "result.json")

    print("[저장 완료]")
    print("- result.csv")
    print("- result.json")

if __name__ == "__main__":
    main()
