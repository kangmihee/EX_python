# 멀티프로세싱을 통한 웹스크래핑

import requests
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool, get_context

def get_links():
    req = requests.get('https://beomi.github.io/beomi.github.io_old/')  # requests : 자료요청
    html = req.text
    #print(html)
    soup = bs(html, 'html.parser')
    my_titles = soup.select('h3 > a')
    data = []
    for title in my_titles:
        data.append(title.get('href'))
        
    return data

def get_content(link):
    aaa_link = 'http://beomi.github.io' + link
    req = requests.get(aaa_link)
    html = req.text
    soup = bs(html, 'lxml')
    print(soup.select('h1')[0].text)
      
if __name__ =='__main__':
    startTime = time.time()
    #print(get_links())
    """
    for link in get_links():
        get_content(link)
    """   
    pool = Pool(processes = 4)
    pool.map(get_content, get_links()) # 수행시간이 훨씬 빠르다! ... get_links()는 값을 받아오는거라 ()필요함
  
    print('---%s seconds ---'%(time.time() - startTime))
    