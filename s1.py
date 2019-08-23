#!/usr/bin/python 

# -*- coding:utf-8 -*-



#import libraries ===================================================================

#python url

import urllib2

# ===================================================================================



class GetData:



  #seoul open api

  url = "http://openapi.elevator.go.kr/openapi/service/ElevatorInformationService/getElevatorList?ServiceKey=3aeLNrMG9KdjsumqSulelgdmCWkU0278EVlfQjwDPLGCp6v6GHkn9ePF7mz03Sw8JtdAMEKhBIlcnNONUpNGVA%3D%3D&numOfRows=1&pageNo=1"



  def main(self):



    try:

      data = urllib2.urlopen(self.url).read()



      #save xml file

      f = open("/var/www/html/data.xml", "w")

      f.write(data)



    except urllib2.HTTPError, e:

      print "HTTP error: %d" % e.code

    except urllib2.URLError, e:

      print "Network error: %s" % e.reason.args[1]



if __name__ == "__main__":

  getData = GetData()

  getData.main()

