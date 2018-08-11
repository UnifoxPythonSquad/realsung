#문제1
"""
1 != 1
 -  1은 1과 다르다는 거짓일 것이므로 결과는 False다.

3 > 1
 - 3이 1보다 크므로 참일 것이다. 결과는 True다.

'a' int 'abc'
 - abc안에 a가 포함되어 있으므로 결과는 True다.

'a' not in [1,2,3]
 - 1,2,3안에 a가 포함되어 있지 않으므로 결과는 True다.
"""
print(1 != 1)
print(3 > 1)
print('a' in 'abc')
print('a' not in [1,2,3])

#문제2
a = "python"
b = ""
c = (1,2,3)
d = 0
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))