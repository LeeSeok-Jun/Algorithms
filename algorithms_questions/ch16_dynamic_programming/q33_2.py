"""
퇴사 - 3회차
"""

# 풀이 제한 시간 : 30분
# 2021/01/25 13:47 ~ 14:14
# 실패 - 내가 틀린 부분 주석처리
# 문제 접근법은 맞았으나 코드 구현법에서 실패

n = int(input())

time = []
profit = []
for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    profit.append(p)

answer = 0
dp = [0] * (n+1)

"""
for i in range(n, -1, -1):
    if time[i-1] + i > n:
        continue

    else:
        dp[i] = profit[i-1]
        
        max_value = 0
        for j in range(i-1, -1, -1):
            if time[j-1] + j < j:
                max_value = max(max_value, profit[j-1])

        dp[i] = dp[i] + max_value
"""

max_value = 0

for i in range(n-1, -1, -1): 
    end_time = i + time[i] 

    if end_time <= n:
        dp[i] = max(profit[i] + dp[end_time], max_value)
        max_value = dp[i]

    else:
        dp[i] = max_value

print(max_value)
# print(max(dp))
# print(dp)