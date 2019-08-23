import urllib2        #urllib2를 불러온다
import BeautifulSoup #방금 설치했던 BeautifulSoup도 불러온다
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
url="http://movie.naver.com/movie/sdb/rank/rmovie.nhn" #내가 파싱할 홈페이지 주소를 url에 넣어준다

soup = BeautifulSoup(urllib2.urlopen(url).read()) #BeautifulSoup를 생성하고 url을 soup에 넣어준다
 #url을 다룰모듈.url을 열어준다.결국 url관련 데이터를 읽어온다고 생각하면 된다
#(괄호안 설명입니다)
pkg_list=soup.findAll("div", "tit3")    #위에서 만들어준 soup(결국은 url임)를 전부 찾아주는데 그중 (div, iti3)
#div값이 tit3인 녀석들을 전부 가져온다는 얘기입니다
#위에서 html 설명보시면 이해가 잘되실껍니다
#결국 url값을 .모두가져오는데 그중 (tit3)의 값을 모두가져와 pkg_list에 넣는다고 보시면 됩니다

count = 1               #이쁘게 하기위해서 카운트를 해줄껍니다 #위 #위 순위 주려고 하는데 0하면 0위부터이니 1로 줍니다

for i in pkg_list:       #pkg_list를 계속 불러와 i에 누적시켜준다

	title = i.findAll('a')    #위에 div tit3만 추출해오면 이쁘지가 않고 지저분한 값까지 전부 긁어오기때문에 지금
                                     #긁어온 값에서 a로 다시한번 쪼개줍니다 현제 tit3을 a로 한번 더 쪼개준셈입니다
#그 값을 title에 넣어준다
	print count, "위: ", str(title)[str(title).find('title="')+7:str(title).find('">')]
#이제 세밀해게 쪼개주는 작업입니다 위에 html코드 보시면 title= 하고 제목나오는 모습이 보이실껍니다
#+7의 이유는 "title="'에서 시작값까지 포함하기 때문에  t i t l e =" 값을 건너뛴 7이 되겠습니다

#또한가지 str해주는이유는 위에서는 soup값을 받아왔기 때문에 문자열로 인식하여야 파이썬이 처리를 하기 때문에 str로 해준다는점입니다


	count=count+1    #이 코드가 없다면 모든 영화가 1위일겁니다. 한번 실행하면 +1로 다음순위가 되도록 +1값을
#올려  줍니다


#출처: https://rednooby.tistory.com/5 [개발자의 취미생활]
