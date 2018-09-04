# iTeRaToR 
> 이터레이터 보고서
> 작성일 : 2018 09 03
> 작성자 : Unifox10기 박성준

![image](./capture/relationships.png)
> 출처 : https://nvie.com/posts/iterators-vs-generators/

> 이터레이터는 반복 가능한 객체를 뜻한다.
> 이터레이션은 이터레이터의 반복 가능한 객체에서 해당 값을 가져오는 행위이다.

###'iter' fuction
> list, dict 타입을 이터레이터로 만들어주는 함수이다.

```python
i = [5,3,1]
print(type(i))
j = iter(i)
print(type(j))
n = 0
while n < 3:
	print(next(j)) 
	n+=1
"""
<type 'list'>
<type 'listiterator'>
5
3
1
"""
```

