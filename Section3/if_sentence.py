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