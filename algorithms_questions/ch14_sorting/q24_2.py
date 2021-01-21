"""
안테나 - 3회차
"""

# 풀이 제한 시간 : 20분
# 2021/01/20 15:36 ~ 15:38
# 정답

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()

print(data[int(len(data)/2)-1])