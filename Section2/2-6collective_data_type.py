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