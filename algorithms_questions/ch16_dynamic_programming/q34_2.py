"""
병사 배치하기 - 3회차
"""

# 풀이 제한 시간 : 40분
# 2021/01/25 14:41 ~ 15:08
# 실패 - 증가하는 부분 수열 알고리즘(LIS)을 응용해야 한다...

n = int(input())
soldiers = list(map(int, input().split()))

dp = [1] * n # i번째 까지 배열을 오름차순으로 만들 때 나올 수 있는 최대 길이 저장

# 입력된 배열을 뒤집어서 대략적으로 오름차순으로 되도록 만듦
soldiers.reverse()

for i in range(1, n):
    for j in range(0, i):
        # 오름차순을 만족하는 경우
        if soldiers[j] < soldiers[i]:
            # 최대 나올 수 있는 부분 수열의 길이 갱신
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))