# Python Section2 code

## 2-1 숫자형

```python
#문제1
lang = 80
eng = 75
math = 55
print((lang + eng + math) / 3)

#문제2
print(17/3)

#문제3
print(17%3)

#문제4
"""
주어진 숫자를 2로 나누어서 나머지가 0이 남으면 짝수, 1이 남으면 홀수 일 것이다.
"""
```

## 2-2 문자열 자료형

```python
#문제 1
print("\"점프 투 파이썬\"")

#문제2
print("Life is too short\nYou need Python")

#문제3
space = " "
print(space*24,"PYTHON")

#문제4
num = "881120-1068234"
ymd = num[:6]
last = num[7:]
print("앞자리 : ",ymd)
print("뒷자리 : ",last)

#문제5
pin = "881120-1068234"
print(pin[7:8])

#문제6
word = "1980M1120"
print(word[4]+word[:4]+word[5:])

#문제7
print("%30s" % "PYTHON")

#문제8
a = "Life is too short, you need python"
print(a.index("short"))

#문제9
index = "a:b:c:d"
print(index.replace(":","#"))

#문제10
a = "a:b:c:d"
b = a.split(":")
c = "#".join(b)
print(c)
```

## 2-3 리스트 자료형

```python
#문제1
i = ['Life', 'is', 'too', 'short', 'you', 'need', 'python']
print(i[4], i[2])

#문제2
j = ['Life', 'is', 'too', 'short']
print(" ".join(j))

#문제3
a = [1, 2, 3]
print(len(a))

#문제4
n = [1, 2, 3]
n.append([4,5])
print("append :",n)
m = [1, 2, 3]
m.extend([4,5])
print("extend :",m);

#문제5
k = [1, 3, 5, 4, 2]
k.sort()
k.reverse()
print(k)

#문제6
l = [1, 2, 3, 4, 5]
l.remove(2)
l.remove(4)
print(l)
```

## 2-4 튜플 자료형
```python
#문제1
t1 = (3,)
print(t1)

#문제2
"""
튜플은 한번 생성하면 그 초기화된 값을 바꿀 수 없다. 
튜플안에 있는 값을 삭제하려거나 다른 값으로 변경하려하면 오류가 난다.
그래서 튜플과 리스트는 값을 변경할수 있는지 없는지 차이를 가지고 있따.
"""

#문제3
t2 = (1,2,3)
print(t2 + (4,))
```

## 2-5 딕셔너리 자료형
```python
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
```

## 2-6 집합 자료형
```python
#문제1
s1 = ['a','b','c']
s2 = set(s1)
print(sorted(s2))

#문제2
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b = set(a)
print(b)

#문제3
n1 = set(['a', 'b', 'c', 'd', 'e'])
n2 = set(['c', 'd', 'e', 'f', 'g'])
result = sorted(n1 - n2)
print(result)

#문제4
i1 = set()
print(type(i1))

#문제5
l = {'a','b','c'}
l.update('d','e','f')
print(sorted(l))
```

## 2-7 불 자료형
```python
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
```

## 2-8 변수
```python
#문제1
a = [1,2,3]
b = [1,2,3]
print(a is b)
#is는 동일한 객체인지를 판별하지 리스트에 있는 값이 같은지는 상관쓰지 않는다.

#문제2
n = [1,2,3]
m = n
print(n is m)
#m = n 이라고 했으니까 m은 n과 같은 주소 값을 가지게 된다.
#그리고 n과 m은 동일한 객체이므로 True를 반환한다.

#문제3
i = j = [1,2,3]
i[1] = 4
print(j)
#i와 j변수는 동일한 리스트 객체를 가르키고 있으므로 i의 값을 바꾸면 j의 값도 변한다.

#문제4
o = [1,2,3]
p = o[:]
print(o is p)
#변수 o는 리스트를 가지고 있는 변수이다. 그러나 변수 P는 o의 리스트 값을 복사했지만,
#p는 o를 가르키고 있지 않고 o와 p는 서로 다른 객체이므로 False를 반환한다.

#문제5
l = [1,2,3]
u = l[:]
l[1] = 4
print(u)
"""
l변수의 인덱스1의 값을 4로 바꾸고 l을 출력하면 1,4,3이 출력될 것이다.
변수 u는 l의 인덱스가 바뀌기 전에 복사하였고 서로 다른 객체이므로 l의 1번째 인덱스 값을
바꿔도 u의 인덱스 값이 바뀌지는 않는다.
"""

#문제6
"""
+기호만을 사용하면 +를 하기 전과 +를 한 후의 주소 값이 다른 것을 확인할 수 있다. (id(변수))
이렇게 +를 사용하면 리스트 값이 변하는게 아니라 두 개의 리스트가 더해져서 새로운 주소 값을 갖는
새로운 리스트가 만들어지는 걸 알 수 있다.
extend를 사용하게되면 extend하기 전과 extend한 후의 주소 값이 같은 것을 확인할 수 있다.
"""

#문제7
t = [1, [2, 3], 4]
y = t[:]
t[1][0] = 5
print(y)
"""
t와 y는 서로 다른 객체이지만 t와 y는 둘 다[2, 3]를 포함하고 있고 서로 같은 곳을 바라보는 객체이다.
그러므로 t의 리스트 값을 변경하면 y가 포함하고 있는 리스트 값도 변경 된다.
"""
```