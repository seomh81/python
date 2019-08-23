#-*- coding: utf-8 -*- 

import xml.etree.ElementTree as ET 
import urllib2 

def subper(sub) : 

    url = 'http://openapi.elevator.go.kr/openapi/service/ElevatorInformationService/getElevatorList?ServiceKey=3aeLNrMG9KdjsumqSulelgdmCWkU0278EVlfQjwDPLGCp6v6GHkn9ePF7mz03Sw8JtdAMEKhBIlcnNONUpNGVA%3D%3D&numOfRows=1&pageNo=1' 
    
    tree = ET.ElementTree(file=urllib2.urlopen(url)) 
    root = tree.getroot() 
    
    return root
    

            
if __name__ == "__main__" : 
    print subper(u'중앙선 회기')
