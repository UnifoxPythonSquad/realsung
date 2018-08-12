# Python Section3 code

## if문
```python
#문제1
money = 5000
card = False
if money >= 4000 or card:
    print("택시를 탈 수 있습니다.")
else:
    print("택시를 탈 수 없습니다.")

#문제2
lucky_list = [1, 9, 23, 46]
if 23 in lucky_list:
    print("야호")

#문제3
num = 123782193799
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

#문제4
i = "나이:30,키:180"
ex = i.split(",")
age = ex[0].split(":")[1]
hgt = ex[1].split(":")[1]
if int(age) < 30 and int(hgt) >= 175:
    print("yes")
else:
    print("no")

#문제5
"""
a = "Life is too short, you need python"
elif 'shirt' not in a:
    print('shirt')
a라는 문장 안에 shirt는 들어가지 않으므로 shirt를 출력할 것이다.
"""
```

## while문
```python
#문제1
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

#문제2
j = 1
result = 0
while j <= 1000:
    if j % 3 ==0:
        result += j
    j += 1
print(result)

#문제3
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
rst = 0
while A:
    n = A.pop()
    if n >= 50:
        rst += n
print(rst)

#문제4
m = 0
while True:
    m += 1
    if m > 4: break
    print("*" * m)

#문제5
l = 7
spe = 0
while l > 0:
    print(' ' * spe + '*' * l)
    spe += 1
    l -= 2
```

## for문
```python
#문제1
for i in range(101):
    print(i)

#문제2
sum = 0
for j in range(1001):
    if j % 5 ==0:
        sum += j
print(sum)

#문제3
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
result = 0
for score in A:
    result += score
avg = result / len(A)
print(avg)

#문제4
h = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
rst = {}
for data in h:
    if data in rst:
        rst[data] += 1
    else:
        rst[data] = 1
print(rst)

#문제5
numbers = [1, 2, 3, 4, 5]
r = [n*2 for n in numbers if n%2==1]
print(r)

#문제6
sen = "Life is too short, you need python"
print("".join([j for j in sen if j not in 'aeiou']))
```