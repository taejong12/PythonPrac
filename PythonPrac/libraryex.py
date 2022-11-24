#sys
import sys
print(sys.argv)


import os
os.environ
os.environ['APPDATA']
os.getcwd()

import shutil
shutil.copy("new.txt","new3.txt")

import time
time.time()
time.localtime(time.time())
time.asctime(time.localtime(time.time()))
time.ctime()
time.strftime('%x',time.localtime(time.time()))
time.strftime('%Y.%m.%d %I:%M:%S %p',time.localtime(time.time()))
#for i in range(10,100):
#    print(i)
#    time.sleep(1)

import calendar
print(calendar.calendar(2022))
calendar.prcal(2022)
calendar.prmonth(2022,11)
calendar.monthrange(2016,2)
import random
random.random()
random.randint(1,10)

#import webbrowser
#webbrowser.open("http://naver.com")

import re
data="""
홍길동의 주민번호는 800905-1049118 입니다.
그리고 고길동의 주민번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))  
    
import datetime

day1=datetime.date(2020,11,11)

import json
with open('info.json') as f:
    data=json.load(f)
print(data)

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.is_strong = False

    def handle_starttag(self, tag, attrs):
        if tag == 'strong':  # <strong> 태그 시작
            self.is_strong = True

    def handle_endtag(self, tag):
        if tag == 'strong':  # </strong> 태그 닫힘
            self.is_strong = False

    def handle_data(self, data):
        if self.is_strong:  # <strong>~</strong> 구간인 경우
            print(data)     # 데이터를 출력

with open('target.html') as f:
    parser=MyHTMLParser()
    parser.feed(f.read())