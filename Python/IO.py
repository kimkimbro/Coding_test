#input()함수는 한 줄의 문자열을 입력받는 함수
n = int(input())

#map()함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
#split() 함수를 이용해서 공백 기준으로 데이터를 나누고
#map() 함수를 각각의 원소를 정수형으로 바꾸고 다시 리스트로 만들어줌

data = list(map(int,input().split()))

#데이터가 정해져 있고 적은 경우
a,b,c = map(int, input().split())


#사용자로부터 입력을 최대한 빠르게 받아야 하는 경우
import sys

data = sys.stdin.readline().rstrip() #엔터가 줄 바꿈 기호로 입력되므로 rstrip()메소드 함께 사용

#자주 사용되는 출력 방법

a=1
b=2
print(a,b)
print('A',end=" ")      #end를 사용하여 줄바꿈X
print('B')

answer = 7
print("정답은 "+str(answer)+"입니다.")

#f-string python3.6부터 사용
answer = 7
print(f"정답은 {answer}입니다.")

