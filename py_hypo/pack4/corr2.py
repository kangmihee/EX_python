# 국내 유료관광지(고궁 5개) 외국인(중국, 미국, 일본) 방문자료로 상관관계 확인

import pandas as pd
import json
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')



# 산점도 그래프 출력 함수
def setScatterGraph(tour_table, all_table, tourPoint):
    # 계산할 관광지에 해당하는 자료만 뽑아 저장하고, 외국인 자료와 병합
    tour = tour_table[tour_table['resNm'] == tourPoint]
    merge_table = pd.merge(tour, all_table, left_index=True, right_index=True)
    print(merge_table.head(2))
    
    # 시각화 
    fig = plt.figure()
    fig.suptitle(tourPoint + ' 상관관계분석용')
    
    # 중국인--------------------------------
    plt.subplot(1, 3, 1)
    plt.xlabel('중국인 입국수')
    plt.ylabel('외국인 입장국수')
    lamd1 = lambda p:merge_table['china'].corr(merge_table['ForNum'])
    r1 = lamd1(merge_table)
    print('r1:',r1)
    plt.title('r={:.5}'.format(r1))
    plt.scatter(merge_table['china'], merge_table['ForNum'], s=6, c='black')
    
    # 일본인--------------------------------
    plt.subplot(1, 3, 2)
    plt.xlabel('일본인 입국수')
    plt.ylabel('외국인 입장국수')
    lamd2 = lambda p:merge_table['japan'].corr(merge_table['ForNum'])
    r2 = lamd2(merge_table)
    print('r2:',r2)
    plt.title('r={:.5}'.format(r2))
    plt.scatter(merge_table['japan'], merge_table['ForNum'], s=6, c='red')
    
    # 미국인--------------------------------
    plt.subplot(1, 3, 3)
    plt.xlabel('미국인 입국수')
    plt.ylabel('외국인 입장국수')
    lamd3 = lambda p:merge_table['usa'].corr(merge_table['ForNum'])
    r3 = lamd3(merge_table)
    print('r3:',r3)
    plt.title('r={:.5}'.format(r3))
    plt.scatter(merge_table['usa'], merge_table['ForNum'], s=6, c='blue')
    
    plt.tight_layout()
    plt.show()
    
    return [tourPoint, r1, r2, r3] # 고궁명(5개), 상관계수 3개반환




def Chulbal():
    # 서울시 관광지 정보를 DataFrame에 저장
    fname = '../testdata/서울특별시_관광지입장정보_2011_2016.json'
    jsonTP = json.loads(open(fname, 'r', encoding='utf-8').read())
    #print(jsonTP) # 한줄로 데이터 나옴
    
    tour_table = pd.DataFrame(jsonTP, columns=('yyyymm','resNm','ForNum'))
    tour_table = tour_table.set_index('yyyymm')
    #print(tour_table)

    resNm = tour_table.resNm.unique()
    print('관광지명 :',resNm[:5])
    
    #-----------------------------------------------------------
    # 중국인 정보를 DataFrame에 저장
    cdf = '../testdata/중국인방문객.json'
    jdata = json.loads(open(cdf, 'r', encoding='utf-8').read())
    
    china_table = pd.DataFrame(jdata, columns=('yyyymm','visit_cnt'))
    china_table = china_table.rename(columns={'visit_cnt':'china'})
    china_table = china_table.set_index('yyyymm')
    print('\nchina_table:\n',china_table[:2])
    
    #-----------------------------------------------------------
    # 일본인 정보를 DataFrame에 저장
    jdf = '../testdata/일본인방문객.json'
    jdata = json.loads(open(jdf, 'r', encoding='utf-8').read())
    
    japan_table = pd.DataFrame(jdata, columns=('yyyymm','visit_cnt'))
    japan_table = japan_table.rename(columns={'visit_cnt':'japan'})
    japan_table = japan_table.set_index('yyyymm')
    print('\njapan_table:\n',japan_table[:2])
    
    #-----------------------------------------------------------
    # 미국인 정보를 DataFrame에 저장
    udf = '../testdata/미국인방문객.json'
    jdata = json.loads(open(udf, 'r', encoding='utf-8').read())
    
    usa_table = pd.DataFrame(jdata, columns=('yyyymm','visit_cnt'))
    usa_table = usa_table.rename(columns={'visit_cnt':'usa'})
    usa_table = usa_table.set_index('yyyymm')
    print('\nusa_table:\n',usa_table[:2])
    
    all_table = pd.merge(china_table, japan_table, left_index=True, right_index=True)
    all_table = pd.merge(all_table, usa_table, left_index=True, right_index=True)
    print('\nall_table:\n',all_table.head(2))
    
    r_list = []
    for tourPoint in resNm[:5]:
        r_list.append(setScatterGraph(tour_table, all_table, tourPoint))
    
    #print(r_list)
    r_table = pd.DataFrame(r_list, columns=('고궁명', '중국','일본','미국'))
    r_table = r_table.set_index('고궁명')
    print('\n',r_table)
    
    # 시각화(막대그래프)
    r_table.plot(kind='bar', rot=50)
    plt.show()
    

if __name__ == '__main__':
    Chulbal()



