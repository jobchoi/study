import os
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# WSL에서 Windows 파일 시스템에 접근하기 위해 /mnt/c/를 사용
chrome_driver_path = "/mnt/c/Users/ROOT/.cache/selenium/chromedriver/win64/120.0.6099.109/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.binary_location = "/usr/bin/google-chrome"  # WSL에서 실행되는 Chrome의 바이너리 경로
driver = webdriver.Chrome(options=options)

def crawl_paper_info(query, num_pages=2, num_papers_per_page=5):
    paper_list = []

    for page in range(num_pages):
        start_index = page * num_papers_per_page
        url = f'https://scholar.google.co.kr/scholar?start={start_index}&q={query}'
        driver.get(url)
        time.sleep(2)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        paper_titles = soup.find_all('h3', {'class': 'gs_rt'})
        num_results = min(num_papers_per_page, len(paper_titles))

        for i in range(num_results):
            paper_title = paper_titles[i].text.strip()
            paper_list.append({'페이지': page + 1, '논문': i + 1, '제목': paper_title})
        print("")

    return paper_list

# 나머지 함수 및 코드는 그대로 유지

# 검색 실행 및 결과 저장
query = 'zinc ion battery'
num_pages = 2
num_papers_per_page = 5
paper_list = crawl_paper_info(query, num_pages, num_papers_per_page)

# 결과를 CSV 파일로 저장
save_to_csv(paper_list)

# 현재 경로에 저장된 CSV 파일을 cat으로 열어서 확인하는 명령어 (WSL 환경에서)
os.system('cat papers.csv')
