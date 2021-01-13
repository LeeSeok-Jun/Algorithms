"""
만들 수 없는 금액 - 3회차
"""

# 풀이 제한 시간 : 30분
# 20201/01/13 14:05 ~ 14:22
# 실패 - 문제 풀이 방식을 어렴풋하게 생각했지만, 코드로 구현하는데는 실패함

n = int(input())
data = list(map(int, input().split()))
data.sort()


# 내가 구현하지 못한 부분
target = 1
for d in data:
    if d > target:
        break
    target += d

print(target)