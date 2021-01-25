"""
편집 거리 - 3회차
"""

# 풀이 제한 시간 : 30분
# 2021/01/25 15:45 ~
# 실패 - 대신 문제에 대한 이해를 하고 넘어가기

a = input()
b = input()

n = len(a)
m = len(b)
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = i

for j in range(1, m+1):
    dp[0][j] = j

for r in range(1, n+1):
    for c in range(1, m+1):
        if a[r-1] == b[c-1]:
            dp[r][c] = dp[r-1][c-1]

        else:
            dp[r][c] = 1 + min(dp[r][c-1], dp[r-1][c-1], dp[r-1][c])

print(dp[n][m])