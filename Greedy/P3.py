# 모험가 길드
# 모험가 N명, 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야함, 여행을 떠날 수 있는 그룹 수의 최대값
# 오름차순 정렬 후 항상 최소한의 모험가의 수만 포함하여 그룹을 결성

N = int(input())
X = list(map(int, input().split()))
X.sort()

count=0
group=0

for i in X:
    group+=1
    if i <= group:
        count+=1
        group=0

print(count)