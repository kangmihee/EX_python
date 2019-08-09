from bs4 import BeautifulSoup
import pandas as pd
#import urllib.request as req
import urllib

# 파싱방법 1 (내가 한거)
# url2 = "https://news.v.daum.net/v/20190726094818902"
# res2 = req.urlopen(url2)
# soup2 = BeautifulSoup(res2, 'lxml')
# 
# price2 = soup2.select("div.news_view > div > section > p")
# #print(price2)
# 
# for i in price2:
#     print(i.string)

#############################################################

# 파싱방법 2 (쓰앵님 방법)
url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
data = urllib.request.urlopen(url).read()

soup = BeautifulSoup(urllib.request.urlopen(url), features="lxml")

title = soup.find('title').string
wf = soup.find('wf')
#city = soup.find_all('city')
city = soup.findAll('city')
cityDatas = []
for c in city:
    #print(c.string)
    cityDatas.append(c.string)
    
df = pd.DataFrame()
df['city'] = cityDatas
print(df.head(3))

#tmEfs = soup.select_one('location > data > tmEf')
tmEfs = soup.select_one('location  data  tmEf')
print(tmEfs)
print(soup.select('data > tmn')[0])

tempMins = soup.select('location > province + city + data > tmn')
print(tempMins)
tempDatas = []
for t in tempMins:
    #print(t.string)
    tempDatas.append(t.string)

df['temp_min'] = tempDatas
df.columns = ['지역', '최저기온']
print(df.head(3))

# 파일로 저장, 불러오기
#df.to_csv('날씨.csv', index = False)
#df2 = pd.read_csv('날씨.csv')
#print(df2)
print()

print(df.head(2))
print(df[0:2])

print(df.head(2))
print(df[-2:len(df)]) # 뒤에서 부터 보기

print(type(df.iloc[0:2]))
print(df.iloc[0:2, :]) # 위랑 같은 코드
print(df.iloc[0:2, 0:1])
print(df.iloc[0:2, 0:2])

print()
print(df.loc[1:3])
print(df.loc[[1,3]])

print()
print(df.info())
print(df['최저기온'].mean())
df = df.astype({'최저기온':'int'})
print(df.info())
print(df['최저기온'].mean())
print(df['최저기온'].std())
print(df['최저기온'].describe())


#############################################################

