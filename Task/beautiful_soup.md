# Python Web Crawling

BeautifulSoap에 대한 자세한 설명과 사용법은 [BeautifulSoap] 공식 문헌을 참고하자

## 크롤링 방법
* 웹 페이지에 request를 보내 결과 html을 받는다.
* 받은 html을 parsing 한다.
* 파싱한 것 중에 필요한 정보만 추출한다.

## Requests

```
$ pip install requests
```
> pip을 이용해 resquests 설치

```python
# requests_parsing.py
#-*- coding: utf-8 -*-
import requests

# HTTP GET Request (블로그 파싱)
request = requests.get('https://realsung.github.io/')

# HTML 소스 가져오기
html_parsing = request.text
print(html_parsing)
print("---"*30)

# HTTP Header 가져오기
header_parsing = request.headers
print(header_parsing)
print("---"*30)

# HTTP Status 가져오기 (출력이 200이면 정상)
http_status = request.status_code
print(http_status)
print("---"*30)

# HTTP가 정상적인지 확인
http_ok = request.ok
print(http_ok)
print("---"*30)
```
> https://realsung.github.io 파싱

## BeautifulSoup
Requests는 단점이 파싱해온 html을 파이썬이 이해하는 객체 구조로 만들어주지 못한다.
위에서 볼 수 있듯이 request.txt는 Python의 문자열 str 객체를 반환하므로 정보를 추출하기 어렵다.

이럴 때는 BeautifulSoup을 이용하면 html 코드를 Python이 이해하는 객체 구조로 변환하는 파싱을 맡고있다.
즉 쉽게 말해 `"의미 있는"`정보를 추출할 수 있다.

```
pip install bs4
```
> pip을 이용해 bs4 설치

```
$ pip install BeautifulSoup
```
> pip을 이용해 BeautifulSoup 설치


```python
#beautifulsoup_parsing.py
#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# HTTP GET Request
request = requests.get('https://realsung.github.io/')

# HTML 소스 가져오기
html = request.text

# BeautifulSoap로 html소스를 python 객체로 변환
# 첫 인자는 html소스코드, 두번째 인자는 어떤 parser를 이용할지 명시
soup = BeautifulSoup(html,'html.parser')
print(soup)
```
이렇게 soup 객체에서 원하는 정보를 찾을 수 있다.

```python
#blog_parsing.py
#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# HTTP GET Request
request = requests.get('https://realsung.github.io/')

html = request.text

soup = BeautifulSoup(html, 'html.parser')

title = soup.select('body > div > div > article > div > h2 > a')
print(title)
```
블로그에 포스팅 되어 있는 글들의 제목들을 parsing 하는 소스

참고해야되는게 blog_parsing.py에서 title은 soup 객체의 리스트이다.

`body > div > div > article > div > h2 > a`
포스팅한 글의 제목을 담고 있는 태그의 selector이다

[BeautifulSoap]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/