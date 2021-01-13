"""
모험가 길드 - 3회차
"""

# 풀이 제한 시간 : 30분
# 2021/01/13 13:26 ~ 13:37

n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)

rest = n
groups = 0

for i in data:
    if i <= rest:
        groups += 1
        rest -= i

print(groups)