import urllib.request
import xml.etree.ElementTree as etree

def main():

    #서울공공데이터사용
    url = "http://openapi.elevator.go.kr/openapi/service/ElevatorInformationService/getElevatorList?ServiceKey=3aeLNrMG9KdjsumqSulelgdmCWkU0278EVlfQjwDPLGCp6v6GHkn9ePF7mz03Sw8JtdAMEKhBIlcnNONUpNGVA%3D%3D" 

    data = urllib.request.urlopen(url).read()

    filename = "elevator.xml"
    f = open(filename, "wb") #다른 사람들의 예제처럼 "w"만 해서 했더니 에러가 발생
    f.write(data)
    f.close()

    #파싱하기
    tree = etree.parse(filename)
    root = tree.getroot()

    for a in root.findall('row'):
        print('소재지1')
        print(a.findtext('address1'))
       
        print('----------------------')

if __name__ == "__main__":
    main()