"""
병사 배치하기 - 2회차
"""

# 풀이 제한 시간 : 40분
# 2020/12/17 10:07 ~ 10:12
# 실패 - 가장 긴 증가하는 부분 수열에 대한 알고리즘 정확하게 기억하기!
# 모든 0 <= j <= i 에 대해서, D[i] = max(D[i], D[j] + 1) if array[j] < array[i]

n = int(input())
array = list(map(int, input().split()))

array.reverse()

dp = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))
