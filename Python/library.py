"""
내장함수: 기본 입출력 함수부터 정렬 함수까지 기본적인 함수 제공
파이썬 프로그램 작성 시 안 되는 필수 기능 포함

itertools: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능 제공
순열과 조합 라이브러리 -> 모든 경우의 수를 고려해야하는 경우, 완전탐색 문제에서 좋음

heapq: 힙 자료구조를 제공
일반적으로 우선순위 큐 기능을 구현하기 위해 사용 ->다익스트라와 같은 최단경로 문제

bisect: 이진 탐색 기능을 제공

collections: 덱, 카운터 등의 유용한 자료구조를 포함

math: 필수적인 수학적 기능을 제공
팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수 포함
"""

#자주 사용되는 내장 함수

result = sum([1,2,3,4,5])       #15
min_result = min([1,2,3,4,5])   #2
max_result = max([1,2,3,4,5])   #7
eval_result = eval("(3+5)*7")   #56

result = sorted([9,1,8,5,4])    #내림차순 정렬
reverse_result = sorted([9,1,8,5,4], reverse=True)  #오름차순 정렬

array = [('홍길동',35), ('이순신',75), ('이무개',50)]
result = sorted(array,key=lambda x:x[1], reverse=True) #오름차순 정렬

#순열: 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것

from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data,3))

from itertools import product
result = list(product(data, repeat=2)) #중복 순열

#조합: 서로 다른 n개에서 순서 상관 없이 서로 다른 r개를 선택하는 것

from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data,2))

from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data,2)) #중복 조합


#Counter 등장횟수를 세능 기능을 제공

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])      #'blue'가 등장한 횟수 
print(counter['green'])     #'green'이 등장한 횟수
print(dict(counter))        #사전 자료형으로 반환

#최대공약수, 최소공배수

import math
def lcm(a,b):
    return a*b//math.gcd(a,b)

print(math.gcd(21,14))
print(lcm(21,14))

