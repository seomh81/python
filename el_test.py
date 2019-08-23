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

soup = BeautifulSoup(html, 'html.parser')

finded_values=soup.find_all('stnm')
[x.text for x in finded_values][:5] # .text를 통해 안의 내용물만을 불러옵니다

#['선진운수종점', '구산동사거리', '한솔아파트입구선정중학교후문', '갈현동미미아파트', '선일여고입구']

startnumber=1
endnumber=1000
CommerceInfor = {}

while endnumber <= 2000:
  print('getting data from %s to %s'%(startnumber,endnumber))
  url='http://openapi.seoul.go.kr:8088/put_your_service_key_here/xml/GetParkInfo/'+str(startnumber)+'/'+str(endnumber)+'/'

  req = requests.get(url)
  html = req.text
  soup = BeautifulSoup(html, 'html.parser')
  
  attr_to_find_list=['parking_code','parking_name','addr','parking_type','que_status','capacity','cur_parking','pay_yn','rates','add_rates']
  for each_attr in attr_to_find_list:
    finded_attr=soup.find_all(each_attr)
    if CommerceInfor.get(each_attr) is None:
      CommerceInfor[each_attr]=[x.text for x in finded_attr]
    else:
      CommerceInfor[each_attr]=CommerceInfor[each_attr]+[x.text for x in finded_attr]

  startnumber += 1000
  endnumber += 1000
    
print('end!')
df = pd.DataFrame(CommerceInfor)

getting data from 1 to 1000
getting data from 1001 to 2000
end!

print(df.shape)
df.head()

(2000, 10)
