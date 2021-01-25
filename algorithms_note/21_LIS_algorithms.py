"""
가장 긴 증가하는 부분 수열(LIS, Longest Increasing Subsequence) 알고리즘
- 다이나믹 프로그래밍의 일종
- 어떤 배열에서 그 배열의 원소들을 선택하여 오름차순으로 정렬된 부분 배열을 만들 때,
  가장 길이가 긴 부분 수열의 길이를 반환하는 알고리즘
- 모든 0 <= j <= i에 대하여, D[i] = max(D[i], D[j] + 1) if array[j] < array[i]
"""

array = [4, 2, 5, 8, 4, 11, 15]

dp = [1] * len(array)

# LIS 알고리즘
for i in range(1, len(array)):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))