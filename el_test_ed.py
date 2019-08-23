import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

key = '3aeLNrMG9KdjsumqSulelgdmCWkU0278EVlfQjwDPLGCp6v6GHkn9ePF7mz03Sw8JtdAMEKhBIlcnNONUpNGVA%3D%3D' ### 여기에 신청한 본인의 key를 넣어야 합니다!
numOfRows='1'
pageNo='1'

queryParams = 'ServiceKey='+key+'&numOfRows='+numOfRows+'&pageNo'+pageNo
url = 'http://openapi.elevator.go.kr/openapi/service/ElevatorInformationService/getElevatorList?'+queryParams

print(url)

#http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?ServiceKey=put_your_service_key_here&busRouteId=100100118 #3. 앞서 Import한 request의 get메소드를 이용하여 respond를 받습니다. (받아온 객체는 Response객체로, 활용을 위해선 추가의 처리를 필요로 합니다)

req = requests.get(url) 
print(type(req))

#<class 'requests.models.Response'> #4. 이 response객체를 텍스트로 변환. 이제 다음과 같이 xml형태의 데이터를 string으로 확인할 수 있습니다.

html = req.text 
print(type(html)) #이제 string객체로 바꼈다.
print(html[:150]) #이렇게 내용물을 확인할 수 있다.

##<?xml version="1.0" encoding="UTF-8" standalone="yes"?><ServiceResult><comMsgHeader/><msgHeader><headerCd>0</headerCd><headerMsg>정상적으로 처리되었습니다.</heade
