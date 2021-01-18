"""
치킨 배달 - 3회차
"""

# 풀이 제한 시간 : 40분
# 2021/01/18 12:47 ~ 13:14
# 정답!

from itertools import combinations

n, m = map(int, input().split())

data = []
home = []
chicken = []
for i in range(n):
    data.append(list(map(int, input().split())))

    for j in range(n):
        if data[i][j] == 1:
            home.append((i, j))
        elif data[i][j] == 2:
            chicken.append((i, j))

answer = int(1e9)
for combination in list(combinations(chicken, m)):
    city_distance = 0

    for h in home:
        chicken_distance = int(1e9)

        for ch in combination:
            chicken_distance = min(chicken_distance, abs(h[0]-ch[0])+abs(h[1]-ch[1]))
        
        city_distance += chicken_distance

    answer = min(answer, city_distance)

print(answer)


