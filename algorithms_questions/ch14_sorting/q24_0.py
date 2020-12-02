"""
안테나
- https://www.acmicpc.net/problem/18310
- 일직선상의 마을에 여러 채의 집이 위치하고 있다.
- 이 중 특정 위치의 집에 특별히 한 개의 안테나를 설치하기로 결정하였다.
- 효율성을 위해 안테나로 부터 모든 집까지의 거리의 총 합이 최소가 되도록 설치하려고 한다.
- 안테나는 집이 위치한 곳에만 설치할 수 있고 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능하다.
- 집들의 위치가 주어질 때, 안테나를 설치할 위치를 선택하는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에 집의 수 N이 자연수로 주어진다.
- 둘째 줄에 N채의 집에 위치가 공백으로 구분되어 자연수로 주어진다.

출력 조건
- 첫째 줄에 안테나를 설치할 위치의 값을 출력한다.
    * 여러 개의 값의 도출될 경우 가장 작은 값을 출력한다.
"""

# 풀이 제한 시간 : 20분
# 2020/12/02 12:02 ~ 12:16
# 실패 - 시간 초과
# 중간에 위치한 집에 안테나를 설치하면 최솟값을 보장받는다!

n = int(input())

data = list(map(int, input().split()))
data.sort(reverse=True)

length = [-1] * (data[0] + 1)

for i in data:
    sum = 0
    for j in data:
        sum += abs(i - j)
    length[i] = sum

answer = []
for i in range(len(length)):
    if length[i] != -1:
        answer.append((i, length[i]))

answer.sort(key = lambda x : x[1])
print(answer[0][0])