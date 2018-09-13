#blog_parsing.py
#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# HTTP GET Request
request = requests.get('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')

html = request.text

soup = BeautifulSoup(html, 'html.parser')

tags = soup.findAll('div', attrs={'class': 'tit3'})

i = 1
for tag in tags :
    print(i ),;print(tag.a.text)
    i+=1

"""
실행결과 :
1 서치
2 상류사회
3 물괴
4 너의 결혼식
5 업그레이
6 목격자
7 더 프레데터
8 신과함께-인과 연
9 어드리프트:우리가 함께한 바다
10 공작
11 안시성
12 맘마미아!2
13 더 게스트
14 명당
15 더 넌
16 협상
17 죄 많은 소녀
18 맞짱
19 미션 임파서블: 폴아웃
20 몰리스 게임
21 원스 어폰 어 타임 인 베니스
22 나비잠
23 베놈
24 82년생 김지영
25 마녀
26 암수살인
27 창궐
28 나를 차버린 스파이
29 바리새인
30 브레이븐
31 타임루프 : 벗어날 수 없는
32 위스키 밴디트
33 더 블랙
34 더 문 앤 더 선
35 엄마친구들 2
36 카메라를 멈추면 안 돼!
37 봄이가도
38 오장군의 발톱
39 미쓰백
40 양말요정 휴고의 대모험
41 오션스8
42 타샤 튜더
43 인랑
44 유전
45 원더풀 고스트
46 일진 2
47 양아치 느와르
48 어느 가족
49 독전
50 메가로돈
"""