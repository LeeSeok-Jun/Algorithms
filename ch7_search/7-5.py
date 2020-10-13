"""
부품 찾기
- 정수 형태의 고유한 번호가 있는 N개의 부품이 있다.
- M개의 부품 종류에 대한 입력이 주어졌을 때 부품이 존재하는지 확인하는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에 정수 N이 주어진다.(1 <= N <= 1,000,000)
- 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다.(1 <= 정수 <= 1,000,000)
- 셋째 줄에는 정수 M이 주어진다.(1 <= M <= 100,000)
- 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다.(1 <= 정수 <= 1,000,000)

출력 조건
- 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를 없으면 no를 출력한다.
"""

# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end: # 작거나 같음! 
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1

    return None

# N(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전제 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행

# M(필요한 부품 종류의 개수) 입력
m = int(input())
# 입력받은 부품의 종류에 대한 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품의 존재 여부 확인
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')