"""
안테나 - 문제 해설
"""

n = int(input())

data = list(map(int, input().split()))

data.sort()

print(data[(n-1) // 2])