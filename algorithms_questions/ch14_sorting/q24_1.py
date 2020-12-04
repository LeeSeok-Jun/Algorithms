"""
안테나 - 2회차
"""

# 풀이 제한 시간 : 20분
# 2020/12/04 11:05 ~ 11:09
# 정답

n = int(input())

data = list(map(int, input().split()))
data.sort()
n = len(data) - 1

print(data[n // 2])