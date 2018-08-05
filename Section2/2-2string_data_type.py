
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