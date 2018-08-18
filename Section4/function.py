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
