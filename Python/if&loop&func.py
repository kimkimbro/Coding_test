###조건문###
#코드의 블록을 들여쓰기로 지정, 탭을 사용하거나 공백문자를 여러번 사용
#스타일 가이드 라인에서 4개의 공백 문자를 사용하는 것을 표준으로 설정

score = 85

if score >= 90:
    print("학점: A")
elif score>=80:
    print("학점: B")
elif score>=70:
    pass                 #pass키워드 -> 아무것도 처리하고 싶지 않을 때
else: print("학점: C")    #조건문 내의 소스코드가 한 줄일 경우 줄 바꿈 하지 않아도 됨

#비교연산자 ==, !=, >, <, >=, <=
#논리연산자 and, or, not
#기타연산자 in, not in -> 리스트, 튜플, 문자열, 딕셔너리 모두 사용 가능

#조건부 표현식을 if~else문을 한 줄에 작성할 수 있도록 해줌
score = 85
result = "Success" if score>=80 else "Fail"
print(result)

#조건문 내 부등식 -> 코드스타일1:x>0 and x<20, 코드스타일2:0<x<20

###반복문###

#while문

i = 1
result = 0

while i<=9:
    if i % 2 ==1:
        result += i
    i+=1

print(result)

#for 문

array = [9, 8, 7, 6, 5]

for x in array:
    print(x)

result=0
for i in range(1,10):
    result += i
print(result)

#continue 키워드 -> 반복문에서 남은 코드의 실행은 건너 뛰고, 다음 반복을 진행하고자 할 때
#break 키워드 -> 반복문 즉시 탈출


###함수###

def add(a,b):
    return a+b


print(add(3,7))
print(add(b=7, a=3))    #파라미터 변수를 직접 지정 가능
print((lambda a,b: a+b)(3,7))   #람다표현식으로 표현

#global 키워드 -> 함수 바깥에 선언된 변수를 바로 참조

#파이썬에서 여러개의 반환 값을 가질 수 있다. C++에서는 포인터나 클래스,구조체를 이용해야함

def operator(a,b):
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b

    return add, sub, mul, div   #packing

a,b,c,d = operator(3,7)     #unpacking
print(a,b,c,d)

#람다 표현식 함수자체를 입력으로 받는 또 다른 함수가 존재할 경우, 한 번만 사용하거나 간단한 경우

array = [('홍길동',50), ('이순신',32), ('이무개',74)]
def my_key(x):
    return x[1]     #두 번째 원소를 기준으로 정렬하기 위해 key 속성 부여
print(sorted(array,key=my_key))
print(sorted(array,key=lambda x:x[1]))

#여러 개의 리스트에 람다 표현식 적용

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a,b: a+b, list1, list2) #각 원소끼리 더한 결과 저장
print(list(result))