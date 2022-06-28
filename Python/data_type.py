###수 자료형###

a=1e9
b=3954e-3
c=5.        #소수부가 0일 때 0생략
b=.7        #정부부가 0일 때 0생략

a=0.3+0.6   #8.99999
print(round(a,4))   #print('%.2f'%3.141592)

# /나누기, #나머지, //몫, **제곱(a<<b),  **0.5제곱근
# ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor), <<(bitwise left shift), >>(bitwise right shift)

###리스트 자료형###
#여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형

#1차원 배열 초기화
n = 10
a = [0]*n

#리스트 컴프리헨션
array1 = [i for i in range(10)]
array2 = [i for i in range(20) if i%2 == 1]
array3 = [i*i for i in range(1,10)]

#2차원 배열 초기화
n = 4
m = 3
array = [[0]*m for _ in range(n)]  #반복문에서 변수 무시할 때 언더바 사용
#cf) array = [[0]*m]*n

a = [1,4,3]          #기본 리스트
a.append(2)          #삽입
a.sort()             #오름차순 정렬
a.sort(reverse=True) #내림차순 정렬
a.reverse()          #원소 뒤집기
a.insert(2,3)        #인덱스 2에 3추가
b=a.count(3)         #값이 3인 데이터 개수
c=a.remove(1)        #값이 1인 데이터 삭제


#특정 값을 가지는 원소 모두 제거(remove 확장)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3,5} #집합 자료형

result = [i for i in a if i not in remove_set]

###문자 자료형###

data = "don't you know \"python\"?"   #"안에 '를 쓸 수 도 있고, \를 통해 쓸 수 있음
print(data)

a = "ABC"
b = "DEF"
print(a+b)      #덧셈을 통해 연결

a = "String"
print(a*3)

a = "ABCDEF"
print(a[2:4])   #문자열 슬라이싱 가능, 문자열은 특정 위치의 값을 변경할 수는 없음

###튜플 자료형###
#한 번 선언된 값을 변경X, 공간의 효율
#서로 다른 성질의 데이터를 묶어서 관리할 때, 데이터의 나열을 해싱의 키값으로 사용할 때, 메모리를 효율적으로 사용해야할 때
a = (1,2,3,4)
print(a[0])
print(a[1:3])

###사전 자료형###
#키와 값의 쌍을 데이터로 가지는 자료형, 리스트 튜플과 다르게 순차X
#변경 불가능한 자료형을 키로 사용, 해시 테이블을 이용하므로 데이터 조회 및 수정에 있어서 O(1)상수시간에 처리가능

#초기화 방법1
data = dict()
data['사과']='Apple'
data['바나나']='Banana'
#초기화 방법2
data ={'사과':'apple', '바나나':'banana'}

#키, 데이터 값 가져오기
key_list = data.keys()
value_list = data.values()

print(list(key_list))       #key 함수는 사전 key라는 객체로 반환되어 list 형태로 바꾸어 줄 수 있다.

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

for key in key_list:
    print(data[key])

###집합자료형###
#중복허용X, 순서X, 리스트 혹은

#데이터 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있음

#문자열을 이용하여 초기화 -> set()함수 이용
data = set([1,1,2,3,4,4,5])

#중관호 안의 각 원소를 ,기준으로 구분하여 삽입하여 초기화
data = {1,1,2,3,4,4,5}

data.add(6)     #새로운 원소 추가
data.updata([5,6])      #새로운 원소 여러 개 추가
data.remove(3)  #특정한 값을 가지는 원소 삭제

a = set([1,2,3,4])
b = set([3,4,5,6])

print(a|b)      #합집합
print(a&b)      #교집합
print(a-b)      #차집합