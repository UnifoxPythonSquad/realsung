#문제1
dic1 = {'name': '홍길동', 'birth': 1128, 'age': 30}
print(dic1)

#문제2
"""
3번째 a[[1]] = 'python'
키로 이용된 [1]은 리스트이므로 변하는 값이다. 
"""

#문제3
dic2 = {'A': 90, 'B': 80, 'C': 70}
dic2_re = dic2.pop('B')
print(dic2)
print(dic2_re)

#문제4
dic3 = {'A': 90, 'B': 80}
print(dic3.get('C',70))

#문제5
dic4 = {'A':90, 'B':80, 'C':70}
print(min(dic4.values()))

#문제6
dic5 = {'A':90, 'B':80, 'C':70}
n = list(dic5.items())
print(n)