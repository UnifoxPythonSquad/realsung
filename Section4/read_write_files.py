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