# Python Section4 code

## 함수
```python
#문제1
def is_odd(num):
    if num % 2 == 0:
        print("짝수")
    else:
        print("홀수")
is_odd(3)

#문제2
def avg(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg(1,2,3,4,5,6,7,8,9,10))

#문제3
def ggdan(j):
    for n in range(1,10):
        print(n*j)

ggdan(3)

#문제4
def pibo(i):
    if i == 0 : return 0
    if i == 1 : return 1
    return pibo(i-2) + pibo(i-1)

for j in range(10):
    print(pibo(j))

#문제5
myfunc = lambda numbers:[num for num in numbers if num > 5]
print(myfunc([2,3,4,5,6,7,8]))
```

## 사용자 입력과 출력
```python
#문제1
input1 = input("첫번째 숫자를 입력하세요 :")
input2 = input("두번째 숫자를 입력하세요 :")
print(int(input1) + int(input2))

#문제2
inputNum = input("숫자를 입력하세요 :")
num = inputNum.split(',')
sum = 0
for i in num:
    sum += int(i)
print(sum)

#문제3
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))
#3번쨰가 다르다.

#문제4
gugu = input("구구단을 출력할 숫자를 입력하세요(2~9) :")
dan = int(gugu)
for i in range(1,10):
    print(dan*i,end=' ')
```

## 파일 읽고 쓰기
```python
#문제1
f1 = open("test.txt", 'w')
f1.write("Life is too short!")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

#문제2
i = input("저장할 내용을 입력하세요 :")
f = open('test.txt', 'a')
f.write(i)
f.close()

#문제3
f = open('abc.txt', 'r')
lines = f.readlines()
f.close()

rlines = reversed(lines)

f = open('abc.txt', 'w')
for line in rlines:
    line = line.strip()
    f.write(line)
    f.write('\n')
f.close()

#문제4
n = open('pro4.txt', 'r')
rp = n.read()
n.close()
rp = rp.replace('java','python')
f = open('pro4.txt', 'w')
f.write(rp)
f.close()

#문제5
f = open("sample.txt")
lines = f.readlines( )
f.close( )
total = 0
for line in lines:
    score = int(line)
    total += score
average = total / len(lines)
f = open("result.txt", "w")
f.write(str(average))
f.close()
```