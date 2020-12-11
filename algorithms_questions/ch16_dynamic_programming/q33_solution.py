"""
퇴사 - 문제 해설
"""

n = int(input())
t = [] # 1번 인덱스부터 저장하기 위함
p = []
dp = [0] * (n+1)
max_value = 0 # 전체 최대 이익

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 n-1 부터 0까지 1씩 줄어들면서 확인
for i in range(n-1, -1, -1):
    time = i + t[i]

    # 상담이 퇴사 전에 끝나는 경우
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    
    # 상담이 퇴사일을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)