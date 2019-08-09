# 기상청 정보(XML) 읽기

import urllib.request
import xml.etree.ElementTree as etree

# try:
#     webdata = urllib.request.urlopen("http://www.kma.go.kr/XML/weather/sfc_web_map.xml")
#     webxml = webdata.read()
#     webxml = webxml.strip().decode("utf-8")
#     print(webxml)
#     #webxml.close()
#      
#     with open('weather.xml', mode='w', encoding='utf-8') as fw:
#         fw.write(webxml)
#      
# except Exception as e:
#     print('err : ', e)


xmlfile = etree.parse('weather.xml')
root = xmlfile.getroot()
print(root.tag)
print(root[0].tag)
children = root.findall("{current}weather") # root[0].tag을 넣어도 됨
print(children)

for it in children:
    y = it.get("year")
    m = it.get("month")
    d = it.get("day")
    h = it.get("hour")
    print(str(y)+"년" + str(m) + "월" + str(d) + "일" + str(h) + "시 현재")

datas = []

for child in root:
    #print(child.tag)
    for it in child:
        print(it.tag)
        local_name = it.text
        re_ta = it.get("ta")
        re_desc = it.get("desc")
        print(local_name + "온도:" + str(re_ta) + " 상태:" + re_desc)
        datas += [[local_name, re_ta, re_desc]]
        
print()
#print(datas)
        
from pandas import DataFrame
df = DataFrame(datas, columns=['지역', '온도', '상태'])
print(df.head(5))









