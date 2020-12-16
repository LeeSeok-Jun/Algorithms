"""
정수 삼각형 - 2회차
"""

# 풀이 제한 시간 : 30분
# 2020/12/16 11:22 ~ 11:30
# 정답 - 1회차 코드가 더 좋은듯...

n = int(input())

dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))


# p[i] = array[i] + max(left_up, up)
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            left_up = 0
        else:
            left_up = dp[i-1][j-1]
        
        if j == i:
            up = 0
        else:
            up = dp[i-1][j]

        dp[i][j] = dp[i][j] + max(left_up, up)

answer = 0
for i in range(n):
    answer = max(answer, dp[n-1][i])

print(answer)