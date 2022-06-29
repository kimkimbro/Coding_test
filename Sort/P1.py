# 두 배열의 원소 교체 문제
# 두 개의 배열 A,B 두 배열은 N개의 자연수 원소로 구성
# 최대 K번의 바꿔치기 연산을 수행, 배열A의 원소 하나와 배열B의 원소 하나를 골라 두 원소를 바꿈
# 배열 A의 모든 원소의 합을 최대로 만듬, 배열 A의 모든 원소의 합을 출력
# 두 배열의 원소가 100000개까지 입력될 수 있으므로 최악의 경우 O(NlogN)을 보장해야 함

n, k = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()    #배열 a는 오름차순 정렬 수행
b.sort(reverse=True)    #배열 b는 내림차순 정렬 수행

for i in range(k):      #첫 번째 인덱스부터 확인하며 두 배열의 원소를 최대 k번 비교
    if a[i]<b[i]:       #a의 원소가 b의 원소보다 작은 경우
        a[i],b[i] = b[i],a[i]   # 두 원소 교체
    else:   #a의 원소가 b의 원소보다 크거나 같을 때 반복문 탈출
        break
print(sum(a))