"""
공유기 설치
- 도현이의 집 N개가 수직선 위에 존재한다. 각각의 집은 좌표를 가지며 같은 좌표를 갖는 경우는 없다.
- 도현이는 집에 공유기 C개를 설치하려고 한다.
- 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치하고 가장 인접한 두 공유기 사이의 거리를 가능한 크게하여 설치하려고 한다.
- C개의 공유기를 N개의 집에 적당히 설치해서 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에 집의 개수 N과 공유기의 개수 C가 하나 이상의 빈 칸을 사이에 두고 주어진다.
- 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 x가 한 줄에 하나 씩 주어진다.

출력 조건
- 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

힌트
- 집의 위치가 [1, 2, 4, 8, 9]이고 공유기의 개수가 3일 때, 공유기를 [1, 4, 8] 또는 [1, 4, 9]에 설치하면,
  가장 인접한 두 공유기 사이의 거리는 3이고, 이 거리보다 크게 공유기를 3개 설치할 수 없다.
"""

# 풀이 제한 시간 : 50분
# 2020/12/09 10:14 ~ 10:41
# 실패 - 메모리 초과

n, c = map(int, input().split())

data = []
for _ in range(n):
    data.append(int(input()))

data.sort()

# 메모리 초과
from itertools import combinations

answer = -1e9
for combination in list(combinations(data, c)):
    min_dist = 1e9

    for i in range(len(combination)-1):
        for j in range(i+1, len(combination)):
            min_dist = min(min_dist, abs(combination[i] - combination[j]))
    
    answer = max(answer, min_dist)

print(answer)