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