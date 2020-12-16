"""
금광 - 2회차
"""

# 풀이 제한 시간 : 30분
# 2020/12/16 11:05 ~ 11:19
# 정답

for _ in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    dp = []
    for i in range(n):
        dp.append(data[i*m:i*m+m])

    # dp[i] = array[i] + max(left_up, left, left_down)
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            
            left = dp[i][j-1]

            dp[i][j] = dp[i][j] + max(left_up, left, left_down)

    answer = 0
    for i in range(n):
        answer = max(answer, dp[i][m-1])

    print(answer)