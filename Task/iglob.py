#-*- coding: utf-8 -*-
import glob
print(glob.glob('*.c'))
#확장자가 .c인 Desktop 디렉토리의 파일들을 출력해준다.
# 출력 결과 : ['tomato.c']


for i in glob.iglob('*'):
	print(i)
# 나는 맥을 써서 그런지 이 코드는 /Users/realsung/Desktop의 모든 파일을 출력했다.


"""
[glob]
glob.glob : 리스트로 반환
glob.iglob : 이터레이터로 반환
디렉토리 내부 파일을 검색할 때 쓰인다.
*,?,[,]와 같은 문자 표현 사용 가능하다.

glob() 함수는 경로에 대응되는 모든 파일 및 디렉토리의 리스트를 반환한다.
glob.iglob() 함수는 glob과 동일한 동작을 수행하지만 리스트로 결과를 반환하지 않고
이터레이를 반환한다. 한번에 모든 결과를 리스트에 담지 않으므로, 결과가 많을 때 유용하다.
"""

"""
.
├── test
│   ├── python_tree.py
│   └── test.c
└── untitled.py

1 directory, 3 files
이런 트리 구조를 glob함수를 이용해 출력할 수 있다.
"""