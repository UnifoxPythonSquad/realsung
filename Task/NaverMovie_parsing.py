#NaverMovie_parsing.py
#-*- coding: utf-8 -*-
import requests
import string
from bs4 import BeautifulSoup

# HTTP GET Request
request = requests.get('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')

html = request.text

soup = BeautifulSoup(html, 'html.parser')

tags = soup.findAll('div', attrs={'class': 'tit3'})

rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
print "___  ___               _        ______                _     _               "
print "|  \/  |              (_)       | ___ \              | |   (_)              "
print "| .  . |  ___  __   __ _   ___  | |_/ /  __ _  _ __  | | __ _  _ __    __ _ "
print "| |\/| | / _ \ \ \ / /| | / _ \ |    /  / _` || '_ \ | |/ /| || '_ \  / _` |"
print "| |  | || (_) | \ V / | ||  __/ | |\ \ | (_| || | | ||   < | || | | || (_| |"
print "\_|  |_/ \___/   \_/  |_| \___| \_| \_| \__,_||_| |_||_|\_\|_||_| |_| \__, |"
print "                                                                       __/ |"
print "                                                                      |___/ "


text = str("")                                                                      

i = 1
for tag in tags:
	if i%6==0:
		print '\n'
	print(i ),;print(tag.a.text),
	i+=1
