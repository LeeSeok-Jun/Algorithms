"""
볼링공 고르기 - 3회차
"""

# 풀이 제한 시간 : 30분
# 2021/01/13 14:25 ~ 14:40
# 실패 - 이중 반복문 사용하면 시간 초과 예상...

n, m = map(int, input().split())
k = list(map(int, input().split()))

# 내가 풀었던 방법
result = 0

for i in range(n):
    for j in range(i+1, n):
        if k[i] != k[j]:
            result += 1

print(result)

# 풀이
data = [0] * (m+1) # 각 볼링공 무게에 대한 리스트 생성
for i in k:
    data[i] += 1 # 각 무게에 대해서 그 수량을 저장

answer = 0

for j in range(1, len(data)):
    n -= data[j] # 전체 볼링공에서 해당 무게의 볼링공 숫자 만큼 뺌
    answer += data[j] * n
    # 한 명이 해당 무게의 볼링공을 선택했을 경우,
    # 다른 사람은 해당 무게의 볼링공 수 * 전체에서 해당 볼링공의 수를 뺀 남은 볼링공의 수만큼 선택할 수 있는 경우의 수가 생긴다.

print(answer)