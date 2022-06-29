#시각 문제
#정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하세요.

N = int(input())

m=[]

for i in range(60):
    m.append(str(i))

count = 0

for hour in range(0,N+1):

    if hour ==3 or hour==13 or hour==23:
        count += (60*60)

    else:
        for minute in m:
            if '3' in minute:
                count+=60
            else:
                for seconds in m:
                    if '3' in seconds:
                        count+=1

print(count)

#모범답안

h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
print(count)