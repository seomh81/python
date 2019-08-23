
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus
#from ubllib.request import urlopen


url = 'http://openapi.elevator.go.kr/openapi/service/ElevatorInformationService/getElevatorList'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '3aeLNrMG9KdjsumqSulelgdmCWkU0278EVlfQjwDPLGCp6v6GHkn9ePF7mz03Sw8JtdAMEKhBIlcnNONUpNGVA%3D%3D', quote_plus('numOfRows') : '10', quote_plus('pageNo') : '1' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print (response_body)
