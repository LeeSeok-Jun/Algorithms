"""
국영수 - 3회차
"""

# 풀이 제한 시간 : 20분
# 2021/01/20 15:24 ~ 15:35
# 정답!

import sys
input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
    data.append(input().split())

data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for d in data:
    print(d[0])