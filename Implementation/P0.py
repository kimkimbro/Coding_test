# 상하좌우 문제
# NxN 크기의 정사각형 공간 위에 서있다. 이 공간은 1X1 크기의 정사각형으로 나누어져 있다.
# 가장 왼 쪽 위(1,1), 가장 오른쪽 아래(N,N), 시작좌표는 (1,1), 상하좌우 방향으로 이동
# L,R,U,D 계획서


#내 답안
N = int(input())
plan = list(input().split())

x, y = 1, 1

for i in plan:
    if i == 'R':
        if(y==N):
            continue
        y+=1
    elif i == 'L':
        if(y==1):
            continue
        y-=1
    elif i == 'U':
        if (x==1):
            continue
        x-=1
    elif i == 'D':
        if(x==N):
            continue
        x+=1

print(x, y)

#모범 답안

n = int(input())
x, y = 1, 1
plans = input().split()

#L,R,U,D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

#이동 계획 하나씩 확인하기
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    # 공간을 벗어나는 경우 무시
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y = nx,ny
print(x,y)        

