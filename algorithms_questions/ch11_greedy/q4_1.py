"""
만들 수 없는 금액 - 2회차
"""

# 2020/11/03 03:33 P.M. ~ 실패
# 정확히 이해하고 다시 풀기!

n = int(input())
coins = list(map(int, input().split()))

coins.sort()

target = 1

### 내가 생각하지 못한 부분 ###
# target 변수에 화폐단위가 작은 것 부터 누적하여 더하는데,
# 다음 화폐 단위가 지금까지 누적한 값보다 크다면 만들 수 없는 최솟값이 된다.
# target은 현재 target-1 까지의 금액을 만들 수 있음을 의미한다!!!

for x in coins:
    if target < x:
        break
    target += x

print(target)