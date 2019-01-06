# -*- coding: utf-8 -*-

#---------------------------------
# kakaobot.py  (상윤 ver)
#---------------------------------

import os
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from PIL import Image

im = Image.open('test1.jpg')
#im.save('python.jpg')

req = requests.get(
      "http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
html = req.text
soup = BeautifulSoup(html, 'html.parser')
soup_ssy = soup.find_all(attrs={'class': 'text_center'})
'''
  for i in soup_ssy:
      print(i.text)
'''

app = Flask(__name__)

@app.route('/keyboard')
def Keyboard():
      dataSend = {
          "type": "buttons",
          "buttons": ["대화하기!", "도움말"]
      }
      return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
      dataReceive = request.get_json()
      content = dataReceive['content']
      if content == u"대화하기!":
          dataSend = {
              "message": {
                  "text": "명령어 목록!\n1. 도움말 \n2. 메뉴 \n3. 연락처 \n4. 메뉴링크,연락처링크\n5. 건학이념\n6. 캠퍼스맵 \n 등등 계속 개발중 "
              }
          }
      elif content == u"도움말":
          dataSend = {
              "message": {
                  "text": "메뉴 , 연락처 , 버스시간 ,건학이념 ,캠퍼스맵 등 의 키워드를 입력해주세요."
              }
          }
      elif u"안녕" in content:
          dataSend = {
              "message": {
                  "text": "안녕하세요 전자공학과 이온입니다. ~_~"
              }
          }
      elif u"이온" in content:
          dataSend = {
              "message": {
                  "text": "전자공학과 s/w 동아리로 다방면으로 많은 활동중"
              }
          }

      elif u"건학이념" in content:
          dataSend = {
              "message": {
                  "photo": {
                      "url": "http://www.kyonggi.ac.kr/uploads/09651eab-35a7-4443-8a5c-7b4f56b636f1.jpg",
                      #"url": "/home/ubuntu/hanion/kakaobot/test1.jpg",
                      "width": 535,
                      "height": 512
                  }
              }

          }
      elif u"캠퍼스맵" in content:
          dataSend = {
              "message": {
                  "photo": {
                      "url": "http://www.kyonggi.ac.kr/web/images/kgu/contents/tour_img_new.jpg",
                      #"url": "/home/ubuntu/hanion/kakaobot/test1.jpg",
                      "width": 800,
                      "height": 512,
                      "text": "1.진리관(대학본부/관광대학) : 정문우측건물\n2.교육관 : 정문에서 우측으로 200m\n3.조리실습동 : 정문에서 우측으로(진리관 뒷편길 이용)\n4.성신관(체육대학) : 정문에서 우측으로 350m\n5.애경관/체육대학 : 정문에서 우측으로 300m\n6.체육관 : 정문에서 우측으로 250m 후 아랫길로 100m 애경관 뒷편\n7.중앙도서관 : 정문에서 정면으로 120m\n8.예지관(인문대학/경상대학) : 정문에서 정면으로 250m\n9.덕문관/법과대학/사회과학대학 : 정문에서 정면으로 250m 후 오른편길로 50m\n10. E-스퀘어 : 정문에서 정면으로 320m(학생식당 및 학생복지공간)\n11.감성코어 : 정문에서 정면으로 120m 후 중앙도서관 옆길로 50m(카페테리아)\n12.광교관(자연과학대학) : 정문에서 정면으로 450m, 혹은 중앙도서관 뒷길로 550m\n13.집현관(공학관) : 정문에서 정면으로 500m, 혹은 중앙도서관 뒷길로 500m\n14.육영관(자연과학관) : 정문에서 정면으로 550m, 혹은 중앙도서관 뒷길로 550m\n15.공과대학 : 정문에서 정면으로 650m, 혹은 후문에서 정면으로 150m 후 우측으로 200m\n16.공학실습동 : 중앙도서관 뒷길로 500m 후 집현관 뒷길 50m\n17.리서치센터 : 정문에서 정면으로 650m 후 공과대학 뒷편, 혹은 후문에서 정면으로 150m 후 우측으로 250m\n18.산학협력단(창업보육센터) : 정문에서 정면으로 550m\n19.종합강의동 : 정문에서 정면으로 350m 후 좌측길로 50m, 혹은 중앙도서관 뒷길로 450m\n20.교수연구동 : 정문에서 중앙도서관 뒷길로 300m\n21.학생회관 : 정문에서 중앙도서관 뒷길로 250m, 혹은 정문에서 좌측으로 200m후 우측으로 100m, 제1복지관 뒤\n22.제1복지관 : 정문에서 좌측으로 200m후 우측으로 100m\n23.어울림관 : 정문에서 좌측으로 200m후 우측으로 100m, 제1복지관 좌측 건물\n24.박물관 : 정문에서 좌측으로 200m후 우측으로 100m, 제1복지관 우측 건물"
                  }
              }

          }
      elif u"캠퍼스맵설명" in content:
          dataSend = {
              "message": {
                  "text": "1.진리관(대학본부/관광대학) : 정문우측건물\n2.교육관 : 정문에서 우측으로 200m\n3.조리실습동 : 정문에서 우측으로(진리관 뒷편길 이용)\n4.성신관(체육대학) : 정문에서 우측으로 350m\n5.애경관/체육대학 : 정문에서 우측으로 300m\n6.체육관 : 정문에서 우측으로 250m 후 아랫길로 100m 애경관 뒷편\n7.중앙도서관 : 정문에서 정면으로 120m\n8.예지관(인문대학/경상대학) : 정문에서 정면으로 250m\n9.덕문관/법과대학/사회과학대학 : 정문에서 정면으로 250m 후 오른편길로 50m\n10. E-스퀘어 : 정문에서 정면으로 320m(학생식당 및 학생복지공간)\n11.감성코어 : 정문에서 정면으로 120m 후 중앙도서관 옆길로 50m(카페테리아)\n12.광교관(자연과학대학) : 정문에서 정면으로 450m, 혹은 중앙도서관 뒷길로 550m\n13.집현관(공학관) : 정문에서 정면으로 500m, 혹은 중앙도서관 뒷길로 500m\n14.육영관(자연과학관) : 정문에서 정면으로 550m, 혹은 중앙도서관 뒷길로 550m\n15.공과대학 : 정문에서 정면으로 650m, 혹은 후문에서 정면으로 150m 후 우측으로 200m\n16.공학실습동 : 중앙도서관 뒷길로 500m 후 집현관 뒷길 50m\n17.리서치센터 : 정문에서 정면으로 650m 후 공과대학 뒷편, 혹은 후문에서 정면으로 150m 후 우측으로 250m\n18.산학협력단(창업보육센터) : 정문에서 정면으로 550m\n19.종합강의동 : 정문에서 정면으로 350m 후 좌측길로 50m, 혹은 중앙도서관 뒷길로 450m\n20.교수연구동 : 정문에서 중앙도서관 뒷길로 300m\n21.학생회관 : 정문에서 중앙도서관 뒷길로 250m, 혹은 정문에서 좌측으로 200m후 우측으로 100m, 제1복지관 뒤\n22.제1복지관 : 정문에서 좌측으로 200m후 우측으로 100m\n23.어울림관 : 정문에서 좌측으로 200m후 우측으로 100m, 제1복지관 좌측 건물\n24.박물관 : 정문에서 좌측으로 200m후 우측으로 100m, 제1복지관 우측 건물"
              }
          }

      elif u"메뉴" in content:
          req = requests.get(
              "http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
          html = req.text
          soup = BeautifulSoup(html, 'html.parser')
          for tag in soup.find_all(attrs={'class': 'text_center'}):
              dataSend = {
                  "message": {
                      "text": "%s" % tag.text.strip()
                  }

              }
      elif content == u"메뉴링크":
          dataSend = {
              "message": {
                  "text": "http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon"
              }
          }
          #크롤링해서 제공할 예정
      elif content == u"연락처링크":
          dataSend = {
              "message": {
                  "text": "http://www.kyonggi.ac.kr/kguTel.kgu?mzcode=K00M00020400"
              }
          }
          #크롤링해서 제공할 예정
      elif u"연락처" in content:
          req = requests.get(
              "http://www.kyonggi.ac.kr/kguTel.kgu?mzcode=K00M00020400")
          html = req.text
          soup = BeautifulSoup(html, 'html.parser')
          for tag in soup.find_all(attrs={'class': 'table_t4'}):
              dataSend = {
                  "message": {
                      "text": "%s" % tag.text.strip()
                  }

              }
          #이하 동문

      elif u"꺼져" in content:
          dataSend = {
              "message": {
                  "text": "볼일 끝났으면 썩 꺼져!"
              }
          }
      else:  # 예외처리 추가해줘야 할 부분 방식 생각해보기
          dataSend = {
              "message": {
                  "text": content
              }
          }
      return jsonify(dataSend)

if __name__ == "__main__":
      app.run(host='0.0.0.0', port=5000)

  #####################################################
