"""
정렬된 배열에서 특정 수의 개수 구하기
- N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
- 이 때, 수열에서 x가 등장하는 횟수를 구하시오.
- 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간초과' 판정을 받는다.

입력 조건
- 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력된다.
- 둘째 줄에 N개의 원소가 정수 형태로 구분되어 입력된다.

출력 조건
- 수열의 원소 중에 값이 x인 원소의 개수를 출력한다.
    * 단 값이 x인 원소가 하나도 없다면 -1을 출력한다.
"""

# 풀이 제한 시간 : 30분
# 2020/12/08 10:40 ~ 10:45

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data = list(map(int, input().split()))

if x in data:
    min_value = bisect_left(data, x)
    max_value = bisect_right(data, x)
    answer = max_value - min_value
else:
    answer = -1

print(answer)