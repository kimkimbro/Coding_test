# 1이 될 때까지
# N-1 or N//k 해서 N이 1이 될 때까지 연산 횟수

# 내 풀이
N, K = map(int, input().split())
count = 0

while (N!=1):
    if (N%K ==0):
        N=N//K
        count+=1
    else:
        N=N-1
        count+=1
print(count)

#모범 답안 -> 시간 복잡도가 로그 시간 복잡도로 줄어듬
n, k = map(int, input().split())

result = 0

while True:

    #n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target=(n//k)*k
    result += (n-target)
    n=target

    #n이 k보다 작을 때(더 이상 나눌 수가 없을 때) 반복문 탈출
    if n<k:
        break

    #k로 나누기
    result+=1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)


