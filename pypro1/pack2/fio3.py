# 동이름으로 주소 찾기

try:
    dong = input('동이름 입력 :')
    #print(dong)
    
    with open('zipcode.txt', mode='r', encoding='euc-kr') as f:
        line = f.readline() # readline은 한줄, readlines는 모두 다 읽어옴
        #print(line)
        while line:
            lines = line.split('\t') # 구분자는 tab
            #print(lines)
            if lines[3].startswith(dong):
                #print(lines)
                print(lines[0] + ' ' + lines[1] + ' ' \
                      + lines[2] + ' ' + lines[3] + ' ' + lines[4])
            line = f.readline()
            
            
       
except Exception as e:
    print('err : ', e)