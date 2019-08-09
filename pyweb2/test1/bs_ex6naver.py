import requests
from bs4 import BeautifulSoup

class Gogo:
    def start(self):
        url = "https://datalab.naver.com/keyword/realtimeList.naver?where=main"
        # 정상요청위해서 Gecko 사용해줌
        page = requests.get(url, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'})
        soup = BeautifulSoup(page.text, 'lxml')
        title = soup.select('span.title')
        print("------네이버 실시간 검색어(전체 연령대) -------")
        count = 0
        for i in title:
            count += 1
            print(str(count) + ") " + i.string) 
               
obj = Gogo()
obj.start()
