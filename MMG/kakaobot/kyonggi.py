# -*- coding: utf-8 -*-

#kakaobot.py  (상윤 ver)

import os
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from PIL import Image

im = Image.open('test1.jpg')
# im.save('python.jpg')

req = requests.get(
    "https://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
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
                "text": "명령어 목록!\n1. 스쿨버스 \n2. 학식 \n3. 캠퍼스맵 \n4. 연락처 \n5. 교육과정 \n6. 홈페이지 \n7. 도서관 \n8. 박물관 \n9. 동아리관련 \n10. 강의시간표\n11. 문의\n12. 와이파이 "
            }
        }
    elif content == u"도움말":
        dataSend = {
            "message": {
                "text": "명령어 목록!\n1. 스쿨버스 \n2. 학식 \n3. 캠퍼스맵 \n4. 연락처 \n5. 교육과정 \n6. 홈페이지 \n7. 도서관 \n8. 박물관 \n9. 동아리관련 \n10. 강의시간표\n11. 문의\n12. 와이파이"
            }
        }    
    elif content == u"help":
        dataSend = {
            "message": {
                "text": "명령어 목록!\n1. 스쿨버스 \n2. 학식 \n3. 캠퍼스맵 \n4. 연락처 \n5. 교육과정 \n6. 홈페이지 \n7. 도서관 \n8. 박물관 \n9. 동아리관련 \n10. 강의시간표\n11. 문의\n12. 와이파이"
            }
        }       
    elif content == u"명령어":
        dataSend = {
            "message": {
                "text": "명령어 목록!\n1. 스쿨버스 \n2. 학식 \n3. 캠퍼스맵 \n4. 연락처 \n5. 교육과정 \n6. 홈페이지 \n7. 도서관 \n8. 박물관 \n9. 동아리관련 \n10. 강의시간표\n11. 문의\n12. 와이파이"
            }
        }       
    elif u"문의" in content:
        dataSend = {
            "message": {
                "text": "https://open.kakao.com/o/gJ07VT1"
            }
        }    
    elif u"피드백" in content:
        dataSend = {
            "message": {
                "text": "https://open.kakao.com/o/gJ07VT1"
            }
        }     
    elif u"스쿨버스" in content:
        dataSend = {
            "message": {
                "text": "고양이버스, 학생통학버스, 통근버스, 방학통학버스 중 필요하신 키워드를 입력해주세요."
            }
        }
    elif content == u"1":
        dataSend = {
            "message": {
                "text": "고양이버스, 학생통학버스, 통근버스, 방학통학버스 중 필요하신 키워드를 입력해주세요."
            }
        }    
    elif content == u"2":
        dataSend = {
            "message": {
                "text": "https://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04025700&restGb=suwon"
            }
        }      
    elif content == u"3":
        dataSend = {
            "message": {
                "text": "찾고자 하는 건물을 입력해주세요.  \n\n 1. 1강의동(진리관) \n 2. 2강의동(성신관) \n 3. 3강의동(애경관) \n 4. 4강의동(예지관) \n 5. 5강의동(덕문관) \n 6. 6강의동(광교관) \n 7. 7강의동(집현관) \n 8. 8강의동(육영관) \n 9. 9강의동(호연관) \n 10. 예학관 \n 11. 공학실습동 (공대실습동) \n 12. 공과대학(제2공학관)\n 13. 리서치센터\n 14. 체육대학 운동장1\n 15. 창업보육센터\n 16. 중앙도서관\n 17. 종합강의동\n 18. 중앙세미나실\n 19. 텔레컨벤션 센터\n 20. 미래관\n 21. 학생회관\n 22. 박물관\n 23. 교수연구동\n 24. 체육관\n 25. 어울림관\n 26. 한우리관\n 27. 경기드림타워\n 28. 홍보관\n 29. 감성코어\n 30. 신한은행"
            }
        }   
    elif content == u"4":
        dataSend = {
            "message": {
                "text": "본인 학과 + 연락처  입력해주세요  \n ex : 00과 연락처"
            }
        }     
    elif content == u"5":
        dataSend = {
            "message": {
                "text": "본인 학과 + 교육과정  입력해주세요  \n ex : 00과 교육과정"
            }
        }     
    elif content == u"6":
        dataSend = {
            "message": {
                "text": "1. 쿠티스\n http://kutis.kyonggi.ac.kr/webkutis/index.jsp\n\n"
                        "2. LMS\n https://lms.kyonggi.ac.kr/login.php\n\n"
                        "3. 가상대학 e-Learning\n http://www.kcucon.or.kr/login/login.asp\n\n"
                        "4. 수강신청\n http://kutis.kyonggi.ac.kr:8080/sugangLink.html\n\n"
                        "5. 경기업\n http://www.kyonggiup.com/main\n\n"
                        "6. 인재 개발처\n http://job.kyonggi.ac.kr/index.jsp\n\n"
                        "7. 교수학습 개발센터\n http://www.kyonggi.ac.kr/KyonggiTpSrv.kgu?cxt=kctl\n\n"
                        "8. 사이버 안전교육\n http://safety.kyonggi.ac.kr/Account/LogOn?rtnUrl=/"
            }
        }     
    elif content == u"7":
        dataSend = {
            "message": {
                "text": "1. 공지사항\n http://library.kyonggi.ac.kr/bbs/list/1\n\n"
                        "2. 소장 자료검색\n http://library.kyonggi.ac.kr/search/tot\n\n"
                        "3. 열람실 좌석현황\n http://libgate.kyonggi.ac.kr/roomstatus/index.asp\n\n"
                        "4. 대출\n http://library.kyonggi.ac.kr/myloan/list\n\n"
                        "5. 희망도서\n http://library.kyonggi.ac.kr/purchaserequest/write\n\n"
                        "6. 도서관 시설예약\n http://library.kyonggi.ac.kr/roomreserve/dateList/1"
            }
        }       
    elif content == u"8":
        dataSend = {
            "message": {
                "text": "http://museum.kyonggi.ac.kr/index.html"
            }
        }      
    elif content == u"박물관":
        dataSend = {
            "message": {
                "text": "http://museum.kyonggi.ac.kr/index.html"
            }
        }     
    elif content == u"9":
        dataSend = {
            "message": {
                "text": "개발중입니다.. 꿀팁 아이디어좀 부탁드립니다."
            }
        }         
    elif u"동아리" in content:
        dataSend = {
            "message": {
              "text": "개발중입니다.. 꿀팁 아이디어좀 부탁드립니다."
            }
        }    
    elif u"강의시간표" in content:
        dataSend = {
            "message": {
              "text": "개발중입니다.. 꿀팁 아이디어좀 부탁드립니다."
            }
        }        
    elif content == u"10":
        dataSend = {
            "message": {
                "text": "개발중입니다.. 꿀팁 아이디어좀 부탁드립니다."
            }
        }       
    elif content == u"11":
        dataSend = {
            "message": {
                "text": "https://open.kakao.com/o/gJ07VT1"
            }
        }       
    elif content == u"12":
        dataSend = {
            "message": {
                "text": "WIFI \nID : kgu_s \nPW : kgu@jump3"
            }
        }      
    elif u"와이파이" in content:
        dataSend = {
            "message": {
                "text": "WIFI \nID : kgu_s \nPW : kgu@jump3"
            }
        }          
    elif u"고양이버스" in content:
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
              "text": "https://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04025700&restGb=suwon"
            }
        }

    elif content == u"캠퍼스맵":
        dataSend = {
            "message": {
                "text": "찾고자 하는 건물을 입력해주세요.  \n\n 1. 1강의동(진리관) \n 2. 2강의동(성신관) \n 3. 3강의동(애경관) \n 4. 4강의동(예지관) \n 5. 5강의동(덕문관) \n 6. 6강의동(광교관) \n 7. 7강의동(집현관) \n 8. 8강의동(육영관) \n 9. 9강의동(호연관) \n 10. 예학관 \n 11. 공학실습동 (공대실습동) \n 12. 공과대학(제2공학관)\n 13. 리서치센터\n 14. 체육대학 운동장1\n 15. 창업보육센터\n 16. 중앙도서관\n 17. 종합강의동\n 18. 중앙세미나실\n 19. 텔레컨벤션 센터\n 20. 미래관\n 21. 학생회관\n 22. 박물관2(지도URL을 원하시면 2를 적어주세요)\n 23. 교수연구동\n 24. 체육관\n 25. 어울림관\n 26. 한우리관\n 27. 경기드림타워\n 28. 홍보관\n 29. 감성코어\n 30. 신한은행"
            }
        }
    elif u"1강의동(진리관)" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507523&urlY=1055980&urlLevel=3&itemId=17566989&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%A7%84%EB%A6%AC%EA%B4%80&srcid=17566989&map_type=TYPE_MAP"
            }
        }
    elif u"1강의동" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507523&urlY=1055980&urlLevel=3&itemId=17566989&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%A7%84%EB%A6%AC%EA%B4%80&srcid=17566989&map_type=TYPE_MAP"
            }
        }
    elif u"2강의동(성신관)" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507437&urlY=1055674&urlLevel=3&itemId=26776098&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%84%B1%EC%8B%A0%EA%B4%80&srcid=26776098&map_type=TYPE_MAP"
            }
        }
    elif u"2강의동" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507437&urlY=1055674&urlLevel=3&itemId=26776098&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%84%B1%EC%8B%A0%EA%B4%80&srcid=26776098&map_type=TYPE_MAP"
            }
        }    
    elif u"3강의동(애경관)" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507588&urlY=1055606&urlLevel=3&itemId=26776099&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%95%A0%EA%B2%BD%EA%B4%80&srcid=26776099&map_type=TYPE_MAP"
            }
        }
    elif u"3강의동" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507588&urlY=1055606&urlLevel=3&itemId=26776099&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%95%A0%EA%B2%BD%EA%B4%80&srcid=26776099&map_type=TYPE_MAP"
            }
        }    
    elif u"4강의동(예지관)" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508085&urlY=1055975&urlLevel=3&itemId=17564292&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%98%88%EC%A7%80%EA%B4%80&srcid=17564292&map_type=TYPE_MAP"
            }
        }
    elif u"4강의동" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508085&urlY=1055975&urlLevel=3&itemId=17564292&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%98%88%EC%A7%80%EA%B4%80&srcid=17564292&map_type=TYPE_MAP"
            }
        }    
    elif u"5강의동(덕문관)" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508151&urlY=1055766&urlLevel=3&itemId=17566587&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EB%8D%95%EB%AC%B8%EA%B4%80&srcid=17566587&map_type=TYPE_MAP"
            }
        }
    elif u"5강의동" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508151&urlY=1055766&urlLevel=3&itemId=17566587&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EB%8D%95%EB%AC%B8%EA%B4%80&srcid=17566587&map_type=TYPE_MAP"
            }
        }    
    elif u"6강의동(광교관)" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508502&urlY=1056046&urlLevel=3&itemId=17562025&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EA%B4%91%EA%B5%90%EA%B4%80&srcid=17562025&map_type=TYPE_MAP"
            }
        }
    elif u"6강의동" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508502&urlY=1056046&urlLevel=3&itemId=17562025&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EA%B4%91%EA%B5%90%EA%B4%80&srcid=17562025&map_type=TYPE_MAP"
            }
        }    
    elif u"7강의동(집현관)" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508602&urlY=1056142&urlLevel=3&itemId=17565835&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%A7%91%ED%98%84%EA%B4%80&srcid=17565835&map_type=TYPE_MAP"
            }
        }
    elif u"7강의동" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508602&urlY=1056142&urlLevel=3&itemId=17565835&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%A7%91%ED%98%84%EA%B4%80&srcid=17565835&map_type=TYPE_MAP"
            }
        }    
    elif u"8강의동(육영관)" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508717&urlY=1056004&urlLevel=3&itemId=17555976&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%9C%A1%EC%98%81%EA%B4%80&srcid=17555976&map_type=TYPE_MAP"
            }
        }
    elif u"8강의동" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508717&urlY=1056004&urlLevel=3&itemId=17555976&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%9C%A1%EC%98%81%EA%B4%80&srcid=17555976&map_type=TYPE_MAP"
            }
        }    
    elif u"9강의동(호연관)" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507526&urlY=1056931&urlLevel=3&itemId=11963159&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%ED%98%B8%EC%97%B0%EA%B4%80&srcid=11963159&map_type=TYPE_MAP"
            }
        }
    elif u"9강의동" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507526&urlY=1056931&urlLevel=3&itemId=11963159&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%ED%98%B8%EC%97%B0%EA%B4%80&srcid=11963159&map_type=TYPE_MAP"
            }
        }    
    elif u"예학관" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507566&urlY=1056597&urlLevel=3&itemId=26776117&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%98%88%ED%95%99%EA%B4%80&srcid=26776117&map_type=TYPE_MAP"
            }
        }
    elif u"공학실습동 (공대실습동)" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508755&urlY=1056126&urlLevel=3&itemId=17567359&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EA%B3%B5%EB%8C%80%EC%8B%A4%EC%8A%B5%EB%8F%99&srcid=17567359&map_type=TYPE_MAP"
            }
        }
    elif u"공학실습동" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508755&urlY=1056126&urlLevel=3&itemId=17567359&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EA%B3%B5%EB%8C%80%EC%8B%A4%EC%8A%B5%EB%8F%99&srcid=17567359&map_type=TYPE_MAP"
            }
        }    
    elif u"공대실습동" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508755&urlY=1056126&urlLevel=3&itemId=17567359&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EA%B3%B5%EB%8C%80%EC%8B%A4%EC%8A%B5%EB%8F%99&srcid=17567359&map_type=TYPE_MAP"
            }
        }    
    elif u"공과대학(제2공학관)" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508866&urlY=1055838&urlLevel=3&itemId=26776119&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%A0%9C2%EA%B3%B5%ED%95%99%EA%B4%80&srcid=26776119&map_type=TYPE_MAP"
            }
        }
    elif u"공과대학" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508866&urlY=1055838&urlLevel=3&itemId=26776119&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%A0%9C2%EA%B3%B5%ED%95%99%EA%B4%80&srcid=26776119&map_type=TYPE_MAP"
            }
        }    
    elif u"제2공학관" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508866&urlY=1055838&urlLevel=3&itemId=26776119&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%A0%9C2%EA%B3%B5%ED%95%99%EA%B4%80&srcid=26776119&map_type=TYPE_MAP"
            }
        }    
    elif u"리서치센터" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=509009&urlY=1056000&urlLevel=3&itemId=17564287&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EB%A6%AC%EC%84%9C%EC%B9%98%EC%84%BC%ED%84%B0&srcid=17564287&map_type=TYPE_MAP"
            }
        }
    elif u"체육대학 운동장1" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507898&urlY=1055751&urlLevel=3&itemId=17580005&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%9A%B4%EB%8F%99%EC%9E%A5&srcid=17580005&map_type=TYPE_MAP"
            }
        }
    elif u"운동장" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507898&urlY=1055751&urlLevel=3&itemId=17580005&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%9A%B4%EB%8F%99%EC%9E%A5&srcid=17580005&map_type=TYPE_MAP"
            }
        }    
    elif u"창업보육센터" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508489&urlY=1055963&urlLevel=3&itemId=26776116&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%B0%BD%EC%97%85%EB%B3%B4%EC%9C%A1%EC%84%BC%ED%84%B0&srcid=26776116&map_type=TYPE_MAP"
            }
        }
    elif u"중앙도서관" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507901&urlY=1056091&urlLevel=3&itemId=8172339&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%A4%91%EC%95%99%EB%8F%84%EC%84%9C%EA%B4%80&srcid=8172339&map_type=TYPE_MAP"
            }
        }
    elif u"종합강의동" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507901&urlY=1056091&urlLevel=3&itemId=8172339&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%A4%91%EC%95%99%EB%8F%84%EC%84%9C%EA%B4%80&srcid=8172339&map_type=TYPE_MAP"
            }
        }
    elif u"중앙세미나실" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507805&urlY=1056106&urlLevel=3&itemId=17562006&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%A4%91%EC%95%99%EC%84%B8%EB%AF%B8%EB%82%98%EC%8B%A4&srcid=17562006&map_type=TYPE_MAP"
            }
        }
    elif u"텔레컨벤션 센터" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507741&urlY=1056416&urlLevel=3&itemId=13571290&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%ED%85%94%EB%A0%88%EC%BB%A8%EB%B2%A4%EC%85%98%EC%84%BC%ED%84%B0&srcid=13571290&map_type=TYPE_MAP"
            }
        }
    elif u"미래관" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507416&urlY=1055812&urlLevel=3&itemId=17567353&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EB%AF%B8%EB%9E%98%EA%B4%80&srcid=17567353&map_type=TYPE_MAP"
            }
        }
    elif u"학생회관" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508019&urlY=1056555&urlLevel=3&itemId=23810963&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%ED%95%99%EC%83%9D%ED%9A%8C%EA%B4%80&srcid=23810963&map_type=TYPE_MAP"
            }
        }
    elif u"박물관2" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507932&urlY=1056496&urlLevel=3&itemId=12665397&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EB%B0%95%EB%AC%BC%EA%B4%80&srcid=12665397&map_type=TYPE_MAP"
            }
        }
    elif u"교수연구동" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508105&urlY=1056308&urlLevel=3&itemId=26776113&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EA%B5%90%EC%88%98%EC%97%B0%EA%B5%AC%EB%8F%99&srcid=26776113&map_type=TYPE_MAP"
            }
        }
    elif u"체육관" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507525&urlY=1055550&urlLevel=3&itemId=17567139&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%B2%B4%EC%9C%A1%EA%B4%80&srcid=17567139&map_type=TYPE_MAP"
            }
        }
    elif u"어울림관" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507970&urlY=1056774&urlLevel=3&itemId=17562007&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%96%B4%EC%9A%B8%EB%A6%BC%EA%B4%80&srcid=17562007&map_type=TYPE_MAP"
            }
        }
    elif u"한우리관" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507390&urlY=1055160&urlLevel=3&itemId=404021031&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EC%88%98%EC%9B%90%EC%BA%A0%ED%8D%BC%EC%8A%A4%20%ED%95%9C%EC%9A%B0%EB%A6%AC%EA%B4%80&srcid=404021031&map_type=TYPE_MAP"
            }
        }
    elif u"경기드림타워" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508555&urlY=1055143&urlLevel=3&itemId=17579635&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EA%B2%BD%EA%B8%B0%EB%93%9C%EB%A6%BC%ED%83%80%EC%9B%8C&srcid=17579635&map_type=TYPE_MAP"
            }
        }
    elif u"홍보관" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507480&urlY=1056449&urlLevel=3&itemId=17564269&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%ED%99%8D%EB%B3%B4%EA%B4%80&srcid=17564269&map_type=TYPE_MAP"
            }
        }
    elif u"감성코어" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=508007&urlY=1056088&urlLevel=3&itemId=24660616&q=%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%20%EA%B0%90%EC%84%B1%EC%BD%94%EC"
            }
        }
    elif u"신한은행" in content:
        dataSend = {
            "message": {
                "text": "http://map.daum.net/?urlX=507956&urlY=1056635&urlLevel=3&itemId=9197981&q=%EC%8B%A0%ED%95%9C%EC%9D%80%ED%96%89%20%EA%B2%BD%EA%B8%B0%EB%8C%80%ED%95%99%EA%B5%90%EC%B6%9C%EC%9E%A5%EC%86%8C&srcid=9197981&map_type=TYPE_MAP"
            }
        }

    elif content == u"연락처":
        dataSend = {
            "message": {
                "text": "본인 학과 + 연락처  입력해주세요  \n ex : 00과 연락처"
            }
        }
    elif content == u"교육과정":
        dataSend = {
            "message": {
                "text": "본인 학과 + 교육과정  입력해주세요  \n ex : 00과 교육과정"
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

    elif u"유아교육과" in content:
        
        if  u"연락처" in content:
            dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010110&orgCd=K010212"
                            }
                        }
            
        elif  u"교육과정" in content:
            dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01011001&orgCd=K010212"
                    }
            }
        else:  # 예외처리 추가해줘야 할 부분 방식 생각해보기
            dataSend = {
              "message": {
                  "text": "연락처 교육과정 test 확인"
              }
           }


    elif u"국어국문학과" in content:
        
            if  u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010101&orgCd=K010201"
                    }
                }
            
            elif  u"교육과정" in content:
                dataSend = {
                    "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010101&orgCd=K010201"
                    }
                }
            
        
    elif u"영어영문학과" in content:
        
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010105&orgCd=K010203"
                    }
                }
            
            elif  u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010501&orgCd=K010203"
                        }
                    }
                
            

    elif u"중어중문학과" in content:
        
            if  u"연락처" in content:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010104&orgCd=K010208"
                }
            }
        
            elif  u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010401&orgCd=K010208"
                        }
                    }
                
            
    elif u"사학과" in content:
        
            if  u"연락처" in content:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010108&orgCd=K010209"
                }
              }
        
            elif  u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010801&orgCd=K010209"
                        }
                    }
                

    elif u"문헌정보학과" in content:

            if  u"연락처" in content:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010109&orgCd=K010210"
                }
            }
        
            elif  u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010901&orgCd=K010210"
                        }
                    }
                

    elif u"문예창작학과" in content:
        
            if  u"연락처" in content:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010102&orgCd=K010211"
                }
            }
        
            elif  u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010201&orgCd=K010211"
                        }
                    }
                
            
    elif u"독어독문전공" in content:
        
            if  u"연락처" in content:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010106&orgCd=K010205"
                }
            }
        
            elif  u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010601&orgCd=K010205"
                        }
                    }
                
            
    elif u"불어불문전공" in content:
        
            if  u"연락처" in content:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010107&orgCd=K010206"
                }
            }
        
            elif  u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010701&orgCd=K010206"
                        }
                    }
                
            
    elif u"일어일문전공" in content:
    
            if  u"연락처" in content:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010103&orgCd=K010207"
                }
            }
        
            elif  u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010301&orgCd=K010207"
                        }
                    }
                
            
    elif u"러시아어문전공" in content:
        
            if  u"연락처" in content:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010111&orgCd=K010214"
                }
            }
        
            elif  u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01011101&orgCd=K010214"
                        }
                    }
                
            
    elif u"서양화미술경영학과" in content:

            if  u"연락처" in content:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010921&orgCd=K011017"
                }
            }
        
            elif  u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01092101&orgCd=K011017"
                        }
                    }
                
            
    elif u"입체조형학과" in content:
        
            if  u"연락처" in content:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010919&orgCd=K011015"
                }
            }
        
            elif  u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01091901&orgCd=K011015"
                        }
                    }
                
            
    elif u"한국화서예학과" in content:
        
            if  u"연락처" in content:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010920&orgCd=K011016"
                }
            }
        
            elif  u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01092001&orgCd=K011016"
                        }
                    }
                
            
    elif u"산업디자인전공" in content:
        
            if u"연락처" in content:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010906&orgCd=K011002"
                }
            }
        
            elif  u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01090601&orgCd=K011002"
                        }
                    }
                
            
    elif u"시각정보디자인전공" in content:
        
            if  u"연락처" in content:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010905&orgCd=K011001"
                }
            }
        
            elif  u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01090501&orgCd=K011001"
                        }
                    }
                
            
    elif u"장신구금속디자인전공" in content:
            if  u"연락처" in content:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010907&orgCd=K011003"
                }
            }
        
            elif  u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01090701&orgCd=K011003"
                        }
                    }
                
            
    elif u"스포츠건강과학전공" in content:
            if  u"연락처" in content:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M011001&orgCd=K011102"
                }
            }
        
            elif  u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01100101&orgCd=K011102"
                        }
                    }

    elif u"레저스포츠전공" in content:
            if  u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M011003&orgCd=K011104"
                }
            }

            elif  u"교육과정" in content:
                    dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01100301&orgCd=K011104"
                        }
                    }


    elif u"스포츠산업경영전공" in content:
            if  u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M011002&orgCd=K011103"
                }
            }

            elif  u"교육과정" in content:
                    dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01100201&orgCd=K011103"
                        }
                    }

    elif u"시큐리티매니지먼트전공" in content:
            if  u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M011004&orgCd=K011105"
                }
            }

            elif  u"교육과정" in content:
                    dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01100401&orgCd=K011105"
                        }
                    }

    elif u"체육학과" in content:
            if  u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M011000&orgCd=K011101"
                }
            }
            elif  u"교육과정" in content:
                    dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01100001&orgCd=K011101"
                        }
                    }

    elif u"법학과" in content:
            if  u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010311&orgCd=K010507"
                }
            }
            elif  u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01031101&orgCd=K010301"
                            }
                        }

    elif u"행정학과" in content:
            if  u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010300&orgCd=K010501"
                    }
                }
            elif  u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01030001&orgCd=K010501"
                            }
                        }

    elif u"경찰행정학과" in content:
            if  u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010304&orgCd=K010505"
                    }
                }
            elif  u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01030401&orgCd=K010505"
                            }
                        }

    elif u"사회복지전공" in content:
            if  u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010301&orgCd=K010502"
                    }
                }
            elif  u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01030101&orgCd=K010502"
                            }
                        }
    elif u"청소년전공" in content:
            if  u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010303&orgCd=K010504"
                    }
                }
            elif  u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01030301&orgCd=K010504"
                            }
                        }
    elif u"국제관계학과" in content:
            if  u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010312&orgCd=K010508"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01031201&orgCd=K010401"
                            }
                        }
    elif u"국제산업정보학과" in content:
            if  u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010313&orgCd=K010509"
                    }
                }
            elif  u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01031301&orgCd=K010403"
                            }
                        }
    elif u"경제전공" in content:
            if  u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010400&orgCd=K010601"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01040001&orgCd=K010601"
                            }
                        }
    elif u"응용통계전공" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010401&orgCd=K010605"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01040101&orgCd=K010605"
                            }
                        }
    elif u"지식재산학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010402&orgCd=K010608"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01040201&orgCd=K010608"
                            }
                        }
    elif u"경영학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010403&orgCd=K010602"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01040301&orgCd=K010602"
                            }
                        }
    elif u"무역학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010404&orgCd=K010603"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01040401&orgCd=K010603"
                            }
                        }
    elif u"회계세무전공" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010405&orgCd=K010604"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01040501&orgCd=K010604"
                            }
                        }
    elif u"경영정보전공" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010406&orgCd=K010606"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01040601&orgCd=K010606"
                            }
                        }
    elif u"수학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010700&orgCd=K010801"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01070001&orgCd=K010801"
                            }
                        }
    elif u"전자물리학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010701&orgCd=K010802"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01070101&orgCd=K010802"
                            }
                        }
    elif u"화학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010702&orgCd=K010803"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01070201&orgCd=K010803"
                            }
                        }
    elif u"생명과학전공" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010703&orgCd=K010804"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01070301&orgCd=K010804"
                        }
                    }
    elif u"식품생물공학전공" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010704&orgCd=K010805"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01070401&orgCd=K010805"
                            }
                        }
    elif u"컴퓨터공학부" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010705&orgCd=K010806"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01070501&orgCd=K010806"
                            }
                        }
    elif u"융합보안학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010001&orgCd=K010102"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01000101&orgCd=K010102"
                            }
                        }
    elif u"토목공공학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010803&orgCd=K010901"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01080301&orgCd=K010901"
                            }
                        }
    elif u"건축학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010802&orgCd=K010902"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01080201&orgCd=K010902"
                            }
                        }
    elif u"건축공학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010801&orgCd=K010903"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01080101&orgCd=K010903"
                            }
                        }
    elif u"산업경영공학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010807&orgCd=K010904"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01080201&orgCd=K010902"
                            }
                        }
    elif u"신소재공학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010810&orgCd=K010905"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01081001&orgCd=K010905"
                            }
                        }
    elif u"환경에너지공학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010804&orgCd=K010906"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01080401&orgCd=K010906"
                            }
                        }
    elif u"전자공학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010805&orgCd=K010907"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01080501&orgCd=K010907"
                            }
                        }
    elif u"도시교통공학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010808&orgCd=K010908"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01080801&orgCd=K010908"
                            }
                        }
    elif u"기계시스템공학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010806&orgCd=K010909"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01080601&orgCd=K010909"
                            }
                        }
    elif u"화학공학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010809&orgCd=K010910"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01080901&orgCd=K010910"
                            }
                        }
    elif u"계약학과" in content:
            if u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010816&orgCd=K010911"
                    }
                }
            elif u"교육과정" in content:
                    dataSend = {
                    "message": {
                        "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01081601&orgCd=K010911"
                            }
                        }
            

    elif u"박물관" in content:
        dataSend = {
            "message": {
                "text": "http://museum.kyonggi.ac.kr/index.html"
            }
        }

    elif content == u"건학이념":
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

    elif content == u"메뉴":
        dataSend = {
            "message": {
                "text":"https://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon"
            }
        }
        # 크롤링해서 제공할 예정
    elif content == u"연락처링크":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguTel.kgu?mzcode=K00M00020400"
            }
        }

    elif u"홈페이지" in content:
        dataSend = {
            "message": {
                "text": "1. 쿠티스\n http://kutis.kyonggi.ac.kr/webkutis/index.jsp\n\n"
                        "2. LMS\n https://lms.kyonggi.ac.kr/login.php\n\n"
                        "3. 가상대학 e-Learning\n http://www.kcucon.or.kr/login/login.asp\n\n"
                        "4. 수강신청\n http://kutis.kyonggi.ac.kr:8080/sugangLink.html\n\n"
                        "5. 경기업\n http://www.kyonggiup.com/main\n\n"
                        "6. 인재 개발처\n http://job.kyonggi.ac.kr/index.jsp\n\n"
                        "7. 교수학습 개발센터\n http://www.kyonggi.ac.kr/KyonggiTpSrv.kgu?cxt=kctl\n\n"
                        "8. 사이버 안전교육\n http://safety.kyonggi.ac.kr/Account/LogOn?rtnUrl=/"
            }
        }

    elif u"도서관" in content:
        dataSend = {
            "message": {
                "text": "1. 공지사항\n http://library.kyonggi.ac.kr/bbs/list/1\n\n"
                        "2. 소장 자료검색\n http://library.kyonggi.ac.kr/search/tot\n\n"
                        "3. 열람실 좌석현황\n http://libgate.kyonggi.ac.kr/roomstatus/index.asp\n\n"
                        "4. 대출\n http://library.kyonggi.ac.kr/myloan/list\n\n"
                        "5. 희망도서\n http://library.kyonggi.ac.kr/purchaserequest/write\n\n"
                        "6. 도서관 시설예약\n http://library.kyonggi.ac.kr/roomreserve/dateList/1"
            }
        }

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

######################################################
