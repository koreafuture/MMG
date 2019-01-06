"""
파이썬으로 크롤링 하기 준비 
환경 : visual studio code
교제 : 파이썬으로 배우는 웹 크롤러, 파이써으로 웹크롤러 만들기
"""
################ 오픈url테스트 #############################################################################################################
"""
from urllib.request import urlopen # urllib라이브러리에서 파이썬 모듈 requst를 읽어 open함수 하나만 임포트
html=urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC+%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%86%A1+%EC%B1%97%EB%B4%87")
#오픈하려는 주소 (나중에 api 주소 입력과 변수설정 추가해서 사용할듯)
print(html.read()) #데이터 읽어드림 (파싱하기 전에 출력 확인)
"""
################## 오픈url 테스 끝#############################################################################################################

"""
beautifulsoup 가 bs4 임 (라이브러리)
크롤링 파싱할떄 쓰는거임 (파싱모듈)

설치법 (윈도우에서) : http://wwww.crummy.com/software/BeautifulSoup/bs4/doc/ 
                   에 들어가서 최신 bs4다운받고 cmd에서 cd로 디렉터리 이동후  >python setup.py install 하면 끝 
                
                 bs가 내장이라고 설치안해도 된다하는데 ModuleNotFoundError: No module named 'bs4' 이라뜸 설치해야함

                 easy_install 이랑 pip는 파이썬 3부터 깔려잇어서 안깔아도됨

    **윈도우에서 설치시 ->(참고 :https://blog.naver.com/panda220/221178698558)

    cmd 에서 내 파이선 깔려잇는 디렉토리로 이동 C:/Users/LG gram/AppData/Local/Programs/Python/Python36 (신상윤 컴터)
    -> 환경변수 path 에 C:/Users/LG gram/AppData/Local/Programs/Python/Python36/Scripts 와 위에꺼 둘다 등록 먼저해야함
          <- 백슬래시 로 입력하면 에러떠서 /로 해둠...
     pip 설치안되잇으면 설치할것. (사진첨부)
     virtualenv로 충돌 방지


"""
########### bs 간단 테스트 #################################################################################################
"""
from urllib.request import urlopen # urllib라이브러리에서 파이썬 모듈 requst를 읽어 open함수 하나만 임포트
from bs4 import BeautifulSoup
html = urlopen("http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
#오픈하려는 주소 (나중에 api 주소 입력과 변수설정 추가해서 사용할듯)
bsObj = BeautifulSoup(html.read(),"html.parser")
print(bsObj.h1) #h1만 걸러서 프린트해주는듯 위에 bs4에서 html로 이쁘게 정리해서
"""
########bs 간단 테스트 완료 #############################################################

########### api 간단 테스트 #################################################################################################
"""
from urllib.request import urlopen # urllib라이브러리에서 파이썬 모듈 requst를 읽어 open함수 하나만 임포트
from bs4 import BeautifulSoup
html = urlopen("http://data.suwon.go.kr/suwon/openapi/service/getDataList.api?serviceId=weatherAreainfo&apiType=json&serviceKey=8e7c858a1cdd4423838f607d3111266e180528224912")
#api 수원시청 내 인증키 넣은거 
bsObj = BeautifulSoup(html.read(),"html.parser")
print(bsObj) #test ㅜㅜ
"""
########  api 간단 테스트 완료 #############################################################

########### api 간단 테스트 lxml #################################################################################################
'''
from urllib.request import urlopen # urllib라이브러리에서 파이썬 모듈 requst를 읽어 open함수 하나만 임포트
from bs4 import BeautifulSoup
html = urlopen("http://data.suwon.go.kr/suwon/openapi/service/getDataList.api?serviceId=weatherAreainfo&apiType=xml&serviceKey=8e7c858a1cdd4423838f607d3111266e180528224912")
#api 수원시청 내 인증키 넣은거 
#api 주소에서 json이나 xml로 받을수있다.
bsObj = BeautifulSoup(html.read(),"lxml")
print(bsObj) #test ㅜㅜ

'''
########  api 간단 테스트 완료 #############################################################

########### api 세계날씨 https://openweathermap.org/api #################################################################################################

# 내 api key    -     11335f1806a57d3a529433bf55ed39e8
'''
from urllib.request import urlopen # urllib라이브러리에서 파이썬 모듈 requst를 읽어 open함수 하나만 임포트
from bs4 import BeautifulSoup
html = urlopen("http://api.openweathermap.org/data/2.5/forecast?id=1835847&APPID=11335f1806a57d3a529433bf55ed39e8&mode=xml") # &mode=xml  seoul
#api 세계날씨
bsObj = BeautifulSoup(html.read(),"lxml")
print(bsObj) #test 
'''
########  세계날씨#############################################################




####################influxdb 연동 ################################################

############ 라이브러리를 설치해 줘야한다
"""
$ pip install influxdb
$ pip install --upgrade influxdb
$ pip uninstall influxdb

"""
############# tutorial - basic ######### 주석안에 주석쓰면 주석풀리네 ㅡㅅㅡ #################################################
"""
# -*- coding: utf-8 -*-

""Tutorial on using the InfluxDB client."

import argparse

from influxdb import InfluxDBClient


def main(host='localhost', port=8086):
    ""Instantiate a connection to the InfluxDB."
    user = 'root'
    password = 'root'
    dbname = 'example'
    dbuser = 'smly'
    dbuser_password = 'my_secret_password'
    query = 'select value from cpu_load_short;'
    json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": "2009-11-10T23:00:00Z",
            "fields": {
                "Float_value": 0.64,
                "Int_value": 3,
                "String_value": "Text",
                "Bool_value": True
            }
        }
    ]

    client = InfluxDBClient(host, port, user, password, dbname)

    print("Create database: " + dbname)
    client.create_database(dbname)

    print("Create a retention policy")
    client.create_retention_policy('awesome_policy', '3d', 3, default=True)

    print("Switch user: " + dbuser)
    client.switch_user(dbuser, dbuser_password)

    print("Write points: {0}".format(json_body))
    client.write_points(json_body)

    print("Querying data: " + query)
    result = client.query(query)

    print("Result: {0}".format(result))

    print("Switch user: " + user)
    client.switch_user(user, password)

    print("Drop database: " + dbname)
    client.drop_database(dbname)


def parse_args():
    ""Parse the args"
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False,
                        default='localhost',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086,
                        help='port of InfluxDB http API')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port)

"""
######### tutorial - basic #############################
"""
########상윤 influx -test ######################

import argparse

from influxdb import InfluxDBClient

client = InfluxDBClient(host='127.0.0.1', port=8086, username='root', password='root', database='ssy2')
client2 = InfluxDBClient(host='127.0.0.1', port=8086, username='root', password='root', database='ssy')
#print("Create database: " + 'ssy2')
#client.create_database('ssy2')
#list2=client2.get_list_database()

#query2 = 'insert weather, location=suwon temp=19,pop=444' insert를 지원안함;;;
#print("Querying data: " + query2)
###client2.query(query2)#############
query = 'select * from weather'
print("Querying data: " + query)
result=client2.query(query)
print("Result: {0}".format(result))
"""

################################################################################
####################### AWS PYTHON DJANGO MySQL ################################
################################################################################