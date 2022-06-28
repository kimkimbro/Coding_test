# 음료수 얼려 먹기
# NxM 크기의 얼음틀 구멍이 뚫려 있는 부분 0, 칸막이가 존재하는 부분1
# 구멍이 뚫려 있는 부분끼리 상하좌우 서로 연결되어 있는 것으로 간주
# 얼음 틀 모양이 주어졌을 때 생성되는 총 아이스크림의 개수 -> 연결 조건 찾기 문제 BFS,DFS

n, m = map(int, input().split())
pan = []
for i in range(n):
    pan.append(list(map(int,input())))      #2차원 리스트 초기화

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:  #주어진 범위를 벗어나는 경우 즉시 종료
        return 0
    if pan[x][y] == 0:              #현재 노드를 아직 방문하지 않았다면
        pan[x][y] = 1               #해당 노드 방문 처리
        #상,하,좌,우의 위치들 모두 재귀적으로 호출 -> 리턴값을 사용하지 않기 때문에 단순히 연결된 모든 노드들의 방문처리 목적
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return 1
    return 0

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == 1:
            result +=1
print(result)



