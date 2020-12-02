"""
국영수 - 문제 풀이
"""

n = int(input())

data = []
for _ in range(n):
    data.append(input().split())

# 차례로 내림차순, 오름차순, 내림차순, 오름차순 정렬
data.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for d in data:
    print(d[0])