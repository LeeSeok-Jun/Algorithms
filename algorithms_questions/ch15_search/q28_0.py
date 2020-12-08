"""
고정점 찾기
- 고정점이란 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미한다.
- 하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며 모든 원소가 오름차순으로 정렬되어 있다.
- 만일 이 수열에서 고정점이 있다면 고정점을 출력하는 프로그램을 작성하시오.
- 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간 초과'판정을 받는다.

입력 조건
- 첫째 줄에 N이 입력된다.
- 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력된다.

출력 조건
- 고정점을 출력한다.
    * 고정점이 없다면 -1을 출력한다.
"""

# 풀이 제한 시간 : 20분
# 2020/12/08 10:55 ~ 11:04
# 실패

from bisect import bisect_left

n = int(input())
data = list(map(int, input().split()))

answer = -1
for i in range(n):
    index = bisect_left(data, i)
    if index == i:
        answer = i-1
    
print(answer)