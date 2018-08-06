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