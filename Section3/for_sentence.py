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