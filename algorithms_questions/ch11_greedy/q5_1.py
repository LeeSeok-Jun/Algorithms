"""
볼링공 고르기 - 2회차
"""

# 2020/11/04 02:38 P.M. ~ 02:52 P.M.
# 정답

n, m = map(int, input().split())

k = list(map(int, input().split()))

data = [0] * (m + 1)

for i in k:
    data[i] += 1

result = 0

for j in range(1, len(data)):
    n -= data[j]
    result += data[j] * n

print(result)
    