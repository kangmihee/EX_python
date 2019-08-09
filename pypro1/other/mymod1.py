# 다른 모듈에서 사용하기 위함

tot = 123

def kbs():
    print('대표방송')
    if __name__ == '__main__':
        print('메인') # 메인 모듈이 아니라 호츌해도 출력 x
    
def Mbc():
    print('문화방송')


