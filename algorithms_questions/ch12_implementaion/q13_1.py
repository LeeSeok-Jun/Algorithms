"""
치킨 배달 - 2회차
"""

# 2020/11/16 12:55 P.M. ~ 01:20 P.M.
# 정답

n, m = map(int, input().split())

city = []
house = []
chicken = []
for r in range(n):
    data = list(map(int, input().split()))
    city.append(data)

    for c in range(len(data)):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

from itertools import combinations # 조합을 사용하기 위해 외장 함수 호출

candidates = list(combinations(chicken, m)) # 조합을 이용하여 리스트 중 m개를 선택하여 후보군 생성

answer = 1e9
for candidate in candidates:
    city_distance = 0

    for h in house:
        chicken_distance = 1e9
        for c in candidate:
            distance = abs(c[0] - h[0]) + abs(c[1]- h[1])
            chicken_distance = min(chicken_distance, distance)
        city_distance += chicken_distance

    answer = min(answer, city_distance)

print(answer)