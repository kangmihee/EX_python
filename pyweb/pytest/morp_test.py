from konlpy.tag import Kkma

kkma = Kkma()
print(kkma.sentences('기준금리 0.25%p 전격인하…성장률 전망도 하향조정'))
print(kkma.nouns('기준금리 0.25%p 전격인하…성장률 전망도 하향조정')) # 단어 끊어서 표현
print(kkma.pos('기준금리 0.25%p 전격인하…성장률 전망도 하향조정'))   # 품사 같이 표현