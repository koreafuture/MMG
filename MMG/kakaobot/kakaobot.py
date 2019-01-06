# -*- coding: utf-8 -*-

# ---------------------------------
# kakaobot.py  (상윤 ver)
# ---------------------------------

import os
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from PIL import Image

im = Image.open('test1.jpg')
# im.save('python.jpg')

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
<<<<<<< HEAD
        "type": "buttons",
        "buttons": ["대화하기!", "도움말"]
=======
        "type" : "buttons",
        "buttons" : ["대화하기!", "도움말", "학사일정"]
>>>>>>> 52e06115e35569b17f865068e0d35d200cde4edf
    }
    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    if content == u"대화하기!":
        dataSend = {
            "message": {
                "text": "명령어 목록!\n1. 스쿨버스 \n2. 학식 \n3. 캠퍼스맵 \n4. 연락처 \n5. 자유게시판\n6. 도서관\n7. 교육과정 Wn8. 쿠티스 링크Wn9. 인재개발처Wn10. 동아리관련Wn11. 박물관Wn12. 강의시간표"
            }
        }
    elif u"스쿨버스" in content:
        dataSend = {
            "message": {
                "text": "고양이버스, 학생통학버스, 통근버스, 방학통학버스 중 필요하신 키워드를 입력해주세요."
            }
        }
<<<<<<< HEAD
    elif u"고양이버스" in content:
=======
    elif content == u"학사일정":
        dataSend = {
            "message": {
                #학사일정 url을 못찾았어요......
            }
        }
    elif u"안녕" in content:
>>>>>>> 52e06115e35569b17f865068e0d35d200cde4edf
        dataSend = {
            "message": {
                "text": "https://www.kyonggi.ac.kr/webService.kgu?menuCode=K00M04002302"
            }
        }
    elif u"학생통학버스" in content:
        dataSend = {
            "message": {
                "text": "https://www.kyonggi.ac.kr/webService.kgu?menuCode=K00M04002303"
            }
        }
    elif u"방학통학버스" in content:
        dataSend = {
            "message": {
                "text": "https://www.kyonggi.ac.kr/webService.kgu?menuCode=K00M04002300"
            }
        }
    elif u"통근버스" in content:
        dataSend = {
            "message": {
                "text": "https://www.kyonggi.ac.kr/webService.kgu?menuCode=K00M04002301"
            }
        }
    elif u"학식" in content:
        dataSend = {
            "message": {
                "https://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04025700&restGb=suwon"
            }
        }
    elif u"캠퍼스맵" in content:
        dataSend = {
            "message": {
                "photo": {
                    "url": "http://www.kyonggi.ac.kr/web/images/kgu/contents/tour_img_new.jpg",
                    # "url": "/home/ubuntu/hanion/kakaobot/test1.jpg",
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

    elif content == u"연락처":
        dataSend = {
            "message": {
                "text": "융합교양대학, 휴먼인재융합대학, 지식정보서비스대학, 융합과학대학, 창의공과대학, 중 필요하신 키워드를 입력해주세요."
            }
        }
    elif u"융합교양대학" in content:
        dataSend = {
            "message": {
                "text": "교직학부, 교양학부 중 필요하신 키워드를 입력해주세요."
            }
        }
    elif content == u"교직학부":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010100&orgCd=K010213"
            }
        }
    elif content == u"교양학부":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010000&orgCd=K010101"
            }
        }
    elif u"휴먼인재융합대학" in content:
        dataSend = {
            "message": {
                "text": "유아교육과, 국어국문학과, 영어영문학과, 중어중문학과, 사학과, 문헌정보학과, 문예창작학과,독어독문전공,불어불문전공,일어일문전공,러시아어문전공,서양화미술격영학과, 입체조형학과, 한국화서예학과, 산업디자인과, 시각정보디자인전공, 장신구금속디자인전공, 스포츠건강과, 레저스포츠전공, 스포츠산업경영전공, 시큐리티매니지먼트전공, 체육학과"
            }
        }
    elif content == u"유아교육과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010110&orgCd=K010212"
            }
        }
    elif content == u"국어국문학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010101&orgCd=K010201"
            }
        }
    elif content == u"영어영문학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010105&orgCd=K010203"
            }
        }
    elif content == u"중어중문학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010104&orgCd=K010208"
            }
        }
    elif content == u"사학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010108&orgCd=K010209"
            }
        }
    elif content == u"문헌정보학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010109&orgCd=K010210"
            }
        }
    elif content == u"문예창작학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010102&orgCd=K010211"
            }
        }
    elif content == u"독어독문전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010106&orgCd=K010205"
            }
        }
    elif content == u"불어불문전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010107&orgCd=K010206"
            }
        }
    elif content == u"일어일문전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010103&orgCd=K010207"
            }
        }
    elif content == u"러시아어문전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010111&orgCd=K010214"
            }
        }
    elif content == u"서양화미술경영학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010921&orgCd=K011017"
            }
        }
    elif content == u"입체조형학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010919&orgCd=K011015"
            }
        }
    elif content == u"한국화서예학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010920&orgCd=K011016"
            }
        }
    elif content == u"산업디자인전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010906&orgCd=K011002"
            }
        }
    elif content == u"시각정보디자인전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010905&orgCd=K011001"
            }
        }
    elif content == u"장신구금속디자인전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010907&orgCd=K011003"
            }
        }
    elif content == u"스포츠건강과학전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M011001&orgCd=K011102"
            }
        }
    elif content == u"레저스포츠전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M011003&orgCd=K011104"
            }
        }
    elif content == u"스포츠산업경영전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M011002&orgCd=K011103"
            }
        }
    elif content == u"시큐리티매니지먼트전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M011004&orgCd=K011105"
            }
        }
    elif content == u"체육학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M011000&orgCd=K011101"
            }
        }

    elif u"지식정보서비스대학" in content:
        dataSend = {
            "message": {
                "text": "법학과, 행정학과, 경찰행정학과, 사회복지전공, 교정보호전공, 청소년전공, 국제관계학과, 국제산업정보학과, 경제전공, 응용통계전공, 지식재산학과, 경영학과, 무역학과, 회계세무전공, 경영정보전공"
            }
        }
    elif content == u"법학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010311&orgCd=K010507"
            }
        }
    elif content == u"행정학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010300&orgCd=K010501"
            }
        }
    elif content == u"경찰행정학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010304&orgCd=K010505"
            }
        }
    elif content == u"사회복지전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010301&orgCd=K010502"
            }
        }
    elif content == u"교정보호전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010304&orgCd=K010505"
            }
        }
    elif content == u"경찰행정학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010304&orgCd=K010505"
            }
        }

    elif content == u"사회복지전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010301&orgCd=K010502"
            }
        }

    elif content == u"교정보호전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010302&orgCd=K010503"
            }
        }
    elif content == u"청소년전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010303&orgCd=K010504"
            }
        }
    elif content == u"국제관계학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010312&orgCd=K010508"
            }
        }
    elif content == u"국제산업정보학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010313&orgCd=K010509"
            }
        }
    elif content == u"경제전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010400&orgCd=K010601"
            }
        }
    elif content == u"응용통계전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010401&orgCd=K010605"
            }
        }
    elif content == u"지식재산학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010402&orgCd=K010608"
            }
        }
    elif content == u"경영학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010403&orgCd=K010602"
            }
        }
    elif content == u"무역학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010404&orgCd=K010603"
            }
        }
    elif content == u"회계세무전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010405&orgCd=K010604"
            }
        }
    elif content == u"경영정보전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010406&orgCd=K010606"
            }
        }
    elif u"융합과학대학" in content:
        dataSend = {
            "message": {
                "text": "수학과, 전자물리학과, 화학과, 생명과학전공, 식품생물공학전공, 컴퓨터공학부, 융합보안학과"
            }
        }
    elif content == u"수학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010700&orgCd=K010801"
            }
        }
    elif content == u"전자물리학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010701&orgCd=K010802"
            }
        }
    elif content == u"화학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010702&orgCd=K010803"
            }
        }
    elif content == u"생명과학전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010703&orgCd=K010804"
            }
        }
    elif content == u"식품생물공학전공":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010704&orgCd=K010805"
            }
        }
    elif content == u"컴퓨터공학부":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010705&orgCd=K010806"
            }
        }
    elif content == u"융합보안학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010001&orgCd=K010102"
            }
        }
    elif u"창의공과대학" in content:
        dataSend = {
            "message": {
                "text": "토목공학과, 건축학과, 건축공학과, 산업경영공학과, 신소재공학과, 환경에너지공학과, 전자공학과, 도시교통학과, 기계시스템공학과, 화학공학과, 건축공학과"
            }
        }
    elif content == u"토목공공학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010803&orgCd=K010901"
            }
        }
    elif content == u"건축학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010802&orgCd=K010902"
            }
        }
    elif content == u"건축공학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010801&orgCd=K010903"
            }
        }
    elif content == u"산업경영공학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010807&orgCd=K010904"
            }
        }
    elif content == u"신소재공학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010810&orgCd=K010905"
            }
        }
    elif content == u"환경에너지공학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010804&orgCd=K010906"
            }
        }
    elif content == u"신소재공학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010810&orgCd=K010905"
            }
        }
    elif content == u"전자공학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010805&orgCd=K010907"
            }
        }
    elif content == u"도시교통공학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010808&orgCd=K010908"
            }
        }
    elif content == u"기계시스템공학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010806&orgCd=K010909"
            }
        }
    elif content == u"화학공학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010809&orgCd=K010910"
            }
        }
    elif content == u"건축공학과":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010816&orgCd=K010911"
            }
        }
    elif u"도서관" in content:
        dataSend = {
            "message": {
                "text": "소개, 전시실, 시설규모, 조직및인력, 관람안내, 찾아오시는길 중 필요하신 키워드를 입력해주세요."
            }
        }
    elif content == u"소개":
        dataSend = {
            "message": {
                "text": "http://museum.kyonggi.ac.kr/inf/inf_index.jsp"
            }
        }
    elif content == u"전시실":
        dataSend = {
            "message": {
                "text": "http://museum.kyonggi.ac.kr/dis/dis_index.jsp"
            }
        }
    elif content == u"시설규모":
        dataSend = {
            "message": {
                "text": "http://museum.kyonggi.ac.kr/inf/inf_sca01.jsp"
            }
        }
    elif content == u"조직및인력":
        dataSend = {
            "message": {
                "text": "http://museum.kyonggi.ac.kr/inf/inf_sys01.jsp"
            }
        }
    elif content == u"관람안내":
        dataSend = {
            "message": {
                "text": "http://museum.kyonggi.ac.kr/inf/inf_gui01.jsp"
            }
        }
    elif content == u"찾아오시는길":
        dataSend = {
            "message": {
                "text": "http://museum.kyonggi.ac.kr/inf/img/inf_subtit_05.gif"
            }
        }
    elif content == u"조직및인력":
        dataSend = {
            "message": {
                "text": "http://museum.kyonggi.ac.kr/inf/inf_sys01.jsp"
            }
        }

    elif content == u"공지사항":
        dataSend = {
            "message": {
                "photo": {
                    "url": "http://www.kyonggi.ac.kr/uploads/09651eab-35a7-4443-8a5c-7b4f56b636f1.jpg",
                    # "url": "/home/ubuntu/hanion/kakaobot/test1.jpg",
                    "width": 535,
                    "height": 512
                }
            }

        }
'''
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
'''            
    elif content == u"메뉴":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon"
            }
        }
        # 크롤링해서 제공할 예정
    elif content == u"연락처링크":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguTel.kgu?mzcode=K00M00020400"
            }
        }
        # 크롤링해서 제공할 예정
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
            # 이하 동문

    elif u"인재개발처" or u"인재" or u"인제" in content: #띄어쓰기하거나 오타가 많이 나올것같아서 or연산자로 묶어봤어요
        dataSend = {
            "message": {
                "text": "http://job.kyonggi.ac.kr/"
            }
        }

    elif u"도서관" in content:
        dataSend = {
            "message": {
                "text": "1. 공지사항\n http://library.kyonggi.ac.kr/bbs/list/1\n"
                        "2. 소장 자료검색\n http://library.kyonggi.ac.kr/search/tot\n"
                        "3. 열람실 좌석현황\n http://libgate.kyonggi.ac.kr/roomstatus/index.asp\n"
                        "4. 대출\n http://library.kyonggi.ac.kr/myloan/list\n"
                        "5. 희망도서\n http://library.kyonggi.ac.kr/purchaserequest/write\n"
                        "6. 도서관 시설예약\n http://library.kyonggi.ac.kr/roomreserve/dateList/1"
            }
        }

    elif u"교육과정" in content: #학과가 너무 많아서 if문을 많이 사용해야될것같아서 좀더 고민해볼게요
        dataSend = {
            "message": {
                "text": content
            }
        }

    elif u"쿠티스" in content:
        dataSend = {
            "message": {
                "text": "http://kutis.kyonggi.ac.kr/webkutis/index.jsp"
            }
        }

    elif u"꺼져" in content:
        dataSend = {
            "message": {
                "text": "볼일 끝났으면 썩 꺼져!"
            }
        }
<<<<<<< HEAD
    else:  # 예외처리 추가해줘야 할 부분 방식 생각해보기
=======
    else: ##예외처리 추가해줘야 할 부분 방식 생각해보기
        #메세지 텍스트로 "오타나 띄어쓰기를 주의해주세요" // "지원하지 않는 메뉴입니다" 이러고 도움말로 넘어가는거 어때요?
>>>>>>> 52e06115e35569b17f865068e0d35d200cde4edf
        dataSend = {
            "message": {
                "text": content
            }
        }
    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

######################################################
