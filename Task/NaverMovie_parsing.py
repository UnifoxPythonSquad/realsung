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
    print(iㅂ ),;print(tag.a.text)
    i+=1