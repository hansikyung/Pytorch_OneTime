## 38. 개발자 화면을 기반으로 웹 크롤링 소스코드 만들기

### 학습목표
#- 1. 웹 크롤링을 위한 HTML의 개발자 화면을 확인한다.
#- 2. 웹 크롤링에 쓰이는 라이브러리를 확인한다.
#- 3. 웹 크롤링 라이브러리를 활용하여 동적 크롤링을 수행한다.

# 라이브러리
# 인터넷에 요청을 전달하고, 결과를 받아오는 라이브러리
import requests

#크롤링을 수행(정적인 크롤링)
from bs4 import BeautifulSoup

#웹드라이버와 상호작용(동적인 크롤링)
from selenium import webdriver

#시간 라이브러리
import time


# url = "https://www.cheongwon.go.kr/portal/petition/open/view?pageIndex=1"

# #request를 통해 웹페이지의 url가져오기
# response = requests.get(url)
# response.encoding = 'utf-8'
# #print(response.text)

# #BeautifulSoup -> 정적인 크롤링(html코드의 구조를 파악, 내용을 선별)
# soup = BeautifulSoup(response.text, 'html.parser')

# #내가 찾고자 하는 class_id로 찾기
# category = soup.find_all('span', class_='category')
# subject = soup.find_all('span', class_='subject')
# petitions = soup.find_all('span', class_='text')

# corpus = []
# for c, s, p in zip(category, subject, petitions):
# 	print(f"Category : {c.text} Subject : {s.text} Content : {p.text}")
# 	corpus.append([s.text, c.text, p.text])
# =========================================================================================

#크롤링 페이지의 수 설정
max_pages = 5

#데이터 저장 리스트
all_corpus = []

for page in range(1, max_pages+1):
	url = f"https://www.cheongwon.go.kr/portal/petition/open/view?pageIndex={page}"

	response = requests.get(url)
	response.encoding = 'utf-8'
	##print(response.text)

	#BeautifulSoup -> 정적인 크롤링(html코드의 구조를 파악, 내용을 선별)
	soup = BeautifulSoup(response.text, 'html.parser')

	#내가 찾고자 하는 class_id로 찾기
	category = soup.find_all('span', class_='category')
	subject = soup.find_all('span', class_='subject')
	petitions = soup.find_all('span', class_='text')

	corpus = []
	for c, s, p in zip(category, subject, petitions):
		print(f"Category : {c.text} Subject : {s.text} Content : {p.text}")
		corpus.append([s.text, c.text, p.text])

	all_corpus.extend(corpus)
	time.sleep(2)

print(f'총 수집된 데이터의 개수 : {len(all_corpus)}')
print(all_corpus[-1])


#모아둔 corpus 저장하기(워드 클라우드를 만들기 위해 실행해야 합니다.)
with open('./crawling_output.txt', 'w', encoding='utf-8') as f:
    for line in all_corpus:
    	for a in line : 
        	f.write(a + '\n')