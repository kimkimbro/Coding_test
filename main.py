data = input().split('-')
num = []

for i in data:
    cnt=0;
    s = i.split('+')
    for a in s:
        cnt+=int(a)
    num.append(cnt)

n=num[0]
for i in range(1,len(num)):
    n-=num[i]

print(n)





