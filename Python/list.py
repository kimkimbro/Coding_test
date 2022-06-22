#1차원 배열 초기화
n = 10
a = [0]*n

#리스트 컴프리헨션
array1 = [i for i in range(10)]
array2 = [i for i in range(20) if i%2 == 1]
array3 = [i*i for i in range(1,10)]

#2차원 배열 초기화
n = 4
m = 3
array = [[0]*m for _ in range(n)]  #반복문에서 변수 무시할 때 언더바 사용
#cf) array = [[0]*m]*n

a = [1,4,3]          #기본 리스트
a.append(2)          #삽입
a.sort()             #오름차순 정렬
a.sort(reverse=True) #내림차순 정렬
a.reverse()          #원소 뒤집기
a.insert(2,3)        #인덱스 2에 3추가
b=a.count(3)         #값이 3인 데이터 개수
c=a.remove(1)        #값이 1인 데이터 삭제


#특정 값을 가지는 원소 모두 제거(remove 확장)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3,5} #집합 자료형

result = [i for i in a if i not in remove_set]







