# 미로 탈출 문제
# NxM 크기의 직사격형 형태 미로, 괴물이 있는 위치는 0, 없는 위치는 1로 표시
# (1,1)에서 출발, 움직여야하는 최소칸의 개수(시작 칸과 마지막 칸 포함)
from collections import deque

n, m = map(int, input().split())
pan = []

for i in range(n):
    pan.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:                #큐가 빌 때까지 반복
        x, y= queue.popleft()

        for i in range(4):      #현재 위치에서 4가지 방향으로 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:  #공간을 벗어나는 경우 무시
                continue
            if pan[nx][ny]==0:      #벽인 경우 무시
                continue
            if pan[nx][ny]==1:      #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                pan[nx][ny] = pan[x][y] + 1
                queue.append((nx,ny))
    return pan[n-1][m-1]

print(bfs(0,0))

