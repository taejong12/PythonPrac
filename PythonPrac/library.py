import datetime

day1=datetime.date(2022,11,22)
print(day1)

import json
with open('info.json') as f:
    data=json.load(f)
print(data)

# 크롤링 지원
from html.parser import HTMLParser #HTML 문서를 파싱해온다

