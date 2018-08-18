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