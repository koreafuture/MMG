### 상윤 크롤링 학식부터 시작

"""
import requests
from bs4 import BeautifulSoup

ssy = requests.get("http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon").text
keywords=BeautifulSoup(ssy,"lxml")
#keywords=keywords.select(" .text_center")
keywords=keywords.select_one(".table_t1")
ssy2=keywords.select_one("td")
print(ssy2)
"""
"""
import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
c = r.content
#print(c)
html = BeautifulSoup(c,"html.parser")

keywords=html.select(" .text_center")
#ssy3 = html.find("div",{"class":"text_center"})
#ssy = html.find(".text_center")
#ssy2= ssy.find("tr")
print(keywords)

tr=html.find("tr")
#print(tr)
td=tr.find_all("td")
#print(td)
"""
#for tr in td:
#    div = tr.find("div",{"class":"text_center"})
#    print(div)
"""    
#sub_contents > table:nth-child(8) > tbody > tr:nth-child(1) > td:nth-child(3)
"""
'''
import requests
from bs4 import BeautifulSoup

req = requests.get("http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_crol = soup.select(
    'tr > td'
)
#print(my_crol)

for ssy in my_crol:
    print(ssy.text)
    #print(ssy.get('td'))
'''
'''
data = {}

for ssy in my_crol:
    data[ssy.text]=ssy.get('href')
'''

################7/12 테스트 '''
'''
import requests
import json
from bs4 import BeautifulSoup

req = requests.get("http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
html = req.text
soup = BeautifulSoup(html, 'html.parser')
soup_ssy = soup.find_all(attrs={'class':'text_center'})
ans=[]

for tr in soup_ssy:
    print(tr.text)
'''    
'''
#for i in soup_ssy:
 #   print(i.text)
'''
'''
#for i in soup_ssy:
#    json_ssy2 = {
#        'menu':[i.text]
#    }

#json_ssy = json.dumps(json_ssy2)
#print(json_ssy2)

'''
#########되는데 제이슨부분 실패 



## 새 방법 파싱 및 제이슨 생성 ㄱㄱ 7/12
'''
import requests
import json
from bs4 import BeautifulSoup

fp = requests.get("http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
source = fp

soup = BeautifulSoup(source)
table = soup.find(id="sub_contents")
trs = table.tbody.find_all('tr')
print(trs)
'''
##############이놈 방식 이상함

##############re re re 7/12
'''
import requests
import json
from bs4 import BeautifulSoup

req = requests.get("http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
html = req.text
soup = BeautifulSoup(html, 'html.parser')
soup_ssy = soup.find_all(attrs={'class':'text_center'})

for tr in soup_ssy:
    tds = tr.find_all('tr')
    #ssy=tds.string
    print(tds)
'''
######################### 영화하는거 비슷하게 해보기 7/12

import requests
import json
from bs4 import BeautifulSoup
'''
req = requests.get("https://www.kyonggi.ac.kr/kguTel.kgu?mzcode=K00M00020400")
html = req.text
soup = BeautifulSoup(html, 'html.parser')
for tag in soup.find_all(attrs={'class':'table_t4'}):
    print(tag.text.strip())
'''

'''

req = requests.get("https://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
html = req.text
soup = BeautifulSoup(html, 'html.parser')
for tag in soup.find_all(attrs={'class': 'text_center'}):
        print("%s") %tag.text.strip()
                
'''
req = requests.get("https://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
html = req.text
soup = BeautifulSoup(html, 'html.parser')
soup_ssy = soup.find_all(attrs={'class': 'table_t1'})

for i in soup_ssy:
      print(i.text)

            
#########################3
'''
import os
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from PIL import Image

im = Image.open('C:/Users/LG gram/Desktop/Hanion/kakaobot/test1.jpg')
im.show()
'''

############################# 크롤링 안되서 뺴둠 0818 ##########
'''
    elif u"메뉴" in content:
        req = requests.get(
            "https://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup.find_all(attrs={'class': 'text_center'}):
            dataSend = {
                "message": {
                    "text": "%s" % tag.text.strip()
                }

            }
'''