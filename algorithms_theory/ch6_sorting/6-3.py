"""
삽입 정렬
- 시간 복잡도 O(N^2)
- 최선의 경우 O(N) : 대부분 정렬이 되있는 경우 삽입 정렬을 사용하는 것이 효과적
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i(start)부터 1(end + 1)까지 1(step)씩 감소하며 반복
        if array[j] < array[j - 1]: # 탐색중인 인덱스의 원소가 앞의 원소보다 작으면 서로 자리 교환
            array[j], array[j - 1] = array[j - 1], array[j] 
        else:
            # 탐색중인 인덱스의 원소가 앞의 원소보다 클 경우 반복 중단
            break

print(array)