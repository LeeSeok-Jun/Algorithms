"""
계수 정렬
- 데이터의 크기 범위가 제한되어 양의 정수 형태로 표현된 경우 사용할 수 있는 매우 빠른 정렬 알고리즘
- 최악의 경우에도 시간 복잡도 O(N + K)
    * 데이터의 개수 N, 최댓값의 크기 K
- 가장 큰 데이터와 가장 작은 데이터의 차이가 너무 크면 사용 불가능
- 모든 범위를 담을 수 있는 크기의 배열을 선언해야 한다.
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
n = len(array)
k = max(array)

count = [0] * (k + 1)

for i in range(n):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')