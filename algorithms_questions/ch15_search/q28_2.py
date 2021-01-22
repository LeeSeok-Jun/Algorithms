"""
고정점 찾기 - 3회차
"""

# 풀이 제한 시간 : 20분
# 2021/01/22 13:27 ~ 13:38
# 정답!

n = int(input())

data = list(map(int, input().split()))

start = 0
end = len(data) - 1
answer = -1

while start <= end:
    mid = (start + end) // 2

    if data[mid] == mid:
        answer = mid
        break

    elif data[mid] < mid:
        start = mid+1

    else:
        end = mid - 1

print(answer)