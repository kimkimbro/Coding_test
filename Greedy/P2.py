# 곱하기 혹은 더하기 문제
# x와 +를 넣어 만들어질 수 있는 가장 큰 수, 모든 연산은 왼쪽에서부터 순서대로 이루어짐


# 내 풀이
S = input()
data=[]

for i in range(len(S)):
    data.append(int(S[i]))

result = 0

for i in range(len(data)-1):
    if(i==0):
        if data[i] ==0 or data[i+1]==0 or data[i]==1 or data[i+1]==1 :
            result=data[i]+data[i+1]
        else:
            result=data[i]*data[i+1]
    else:
        if data[i + 1] == 0 or data[i+1]==1:
            result += data[i+1]
        else:
            result *= data[i + 1]

print(result)

# 모범 답안

data = input()

#첫 번째 수를 숫자로 변경하여 대임
result2 = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기 보다 더하기 수행
    if num<=1 or result2 <=1:
        result2 += num
    else:
        result2 *=num
print(result2)