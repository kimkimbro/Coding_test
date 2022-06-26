#문자열 재정렬
#알파벳 대문자와 숫자(0~9)로만 구성된 문자열 입력
#알파벳을 오름차순으로 정렬하여 출력한 뒤, 그 뒤에 모든 숫자값을 더해 이어 출력 K1KA5CB7 -> ABCKK13

#내 풀이
data = input()

num = ['0','1','2','3','4','5','6','7','8','9']
result = []
summary=0

for i in range(len(data)):
    if data[i] in num:
        summary+=int(data[i])
    else:
        result.append(data[i])


result.sort()
output=""

for i in result:
    output+=i
if summary != 0:
    summary = str(summary)
    output+=summary

print(output)

#모범답안

data = input()
result=[]
value = 0

for x in data:
    if x.isalpha():     ###isalpha() 라이브러리
        result.append(x)
    else:
        value+=int(x)

result.sort()

if value !=0:
    result.append(str(value))
print(''.join(result))      ###join함수  list->문자열

