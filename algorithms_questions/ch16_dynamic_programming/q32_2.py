"""
정수 삼각형 - 3회차
"""

# 풀이 제한 시간 : 30분
# 2021/01/25 13:40 ~ 13:47
# 정답

n = int(input())

dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

for r in range(1, n):
    for c in range(len(dp[r])):
        if c == 0:
            left_up = 0
        else:
            left_up = dp[r-1][c-1]

        if c == len(dp[r])-1:
            right_up = 0
        else:
            right_up = dp[r-1][c]

        dp[r][c] = dp[r][c] + max(left_up, right_up)

print(max(dp[n-1]))