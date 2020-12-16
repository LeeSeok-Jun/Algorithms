"""
퇴사 - 2회차
"""

# 풀이 제한 시간 : 30분
# 2020/12/16 11:33 ~ 
# 실패 - 점화식의 유도와 그 의미를 정확하게 이해하지 못함...

n = int(input())

time = []
profit = []

for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    profit.append(p)

dp = [0] * (n + 1)
max_value = 0 # 마지막날 부터 계산 시 현재까지의 최대 상담 금액

# 점화식 : dp[i] = max(p[i] + dp[ t[i] + i ], max_value)
# i번째날 얻을 수 있는 최대 이익은 i번째 날 일하면 얻을 수 있는 이익과 다음에 일할 수 있는 날의 최대 이익을 더하고
# 지금까지의 최대 이익과 비교하여 더 큰 값을 취힌다.

# 마지막 날 부터 확인
for i in range(n-1, -1, -1):
    time = time[i] + i # 다음 상담에 대한 날짜

    # 다음 상담이 기간 안에 가능한 일이면
    # i번째 날에 얻을 수 있는 최대 이익을 계산 가능
    if time <= n:
        dp[i] = max(profit[i] + dp[time], max_value)
        max_value = dp[i] # 최대 이익을 저장함(변할 수도 있고 안 변할 수도 있다.)

    # 다음 상담이 기간 내에 불가능한 일이면
    # i-1 번재 날에 얻을 수 있는 최대 이익은 기존에 계산된 최대 이익
    else:
        dp[i] = max_value

print(max_value)