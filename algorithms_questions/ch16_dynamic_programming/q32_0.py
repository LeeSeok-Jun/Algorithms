"""
정수 삼각형
- https://www.acmicpc.net/problem/1932
"""

# 풀이 제한 시간 : 30분
# 2020/12/11 11:00 ~ 11:14
# 정답

n = int(input())

# 점화식 : dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i-1][j])
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            left_up = 0
        else:
            left_up = dp[i-1][j-1]
        
        if j == len(dp[i]) - 1:
            right_up = 0
        else:
            right_up = dp[i-1][j]

        dp[i][j] = dp[i][j] + max(left_up, right_up)

answer = 0
for d in dp[n-1]:
    answer = max(answer, d)

print(answer)