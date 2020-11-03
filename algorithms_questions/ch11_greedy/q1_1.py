"""
모험가 길드 - 2회차
"""

# 2020/11/03 03:12 P.M. ~ 03:17 P.M.
# 정답

n = int(input())

data = list(map(int, input().split()))

data.sort()
groups = 0
member = 0

for i in data:
    member += 1
    if member >= i:
        groups += 1
        member = 0

print(groups)