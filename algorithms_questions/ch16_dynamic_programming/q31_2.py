"""
금광 - 3회차
"""

# 풀이 제한 시간 : 30분
# 2021/01/25 13:18 ~ 13:33
# 정답!


for tc  in range(int(input())):
    n, m = map(int, input().split())

    data = list(map(int, input().split()))

    dp = [[] for _ in range(n)]
    for i in range(n):
        dp[i] = data[i*m: i*m+m]

    for c in range(1, m):
        for r in range(n):
            if r == 0:
                left_up = 0
            else:
                left_up = dp[r-1][c-1]
            
            if r == n-1:
                left_down = 0
            else:
                left_down = dp[r+1][c-1]

            left = dp[r][c-1]

            # dp[r][c] = max(dp[r][c] + left_up, dp[r][c] + left, dp[r][c] + left_down)
            dp[r][c] = dp[r][c] + max(left_down, left, left_up) # 이 방법이 보다 효율적

    answer = 0
    for r in range(n):
        answer = max(answer, dp[r][m-1])

    print(answer)