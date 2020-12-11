"""
퇴사
- https://www.acmicpc.net/problem/14501
"""

# 풀이 제한 시간 : 30분
# 2020/12/11 11:17 ~ 11:30
# 문제 접근 방식이 잘못됨(거꾸로 생각하기!)

"""
n = int(input())

array = []
for _ in range(n):
    t, p = map(int, input().split())
    array.append((t, p))

dp = [0] * (n+1)
for i in range(1, n+1):
    now_time = array[i][0]
    now_profit = array[i][1]

    for j in range(n+1):
        if j > now_time:
            now_time
"""