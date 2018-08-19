# Python Section5 code

# 클래스
```python
#문제1
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val
cal = Calculator()
cal.add(3)
cal.add(4)
print(cal.value)

#문제2
class Calculator2:
    def __init__(self, init_value=0):
        self.value = init_value
    def add(self, val):
        self.value += val
cal = Calculator2()
cal.add(3)
cal.add(4)
print(cal.value)

#문제3
class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
prin = UpgradeCalculator()
prin.minus(4)
prin.minus(3)
print(prin.value)

#문제4
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

#문제5
class Calculator3:
    def __init__(self, numberList):
        self.numberList = numberList

    def sum(self):
        result = 0
        for num in self.numberList:
            result += num
        return result

    def avg(self):
        total = self.sum( )
        return total / len(self.numberList)
```