"""
카드 정렬하기
- N개의 숫자 카드 묶음의 각각 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지 구하는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에 N이 주어진다.
- 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다.

출력 조건
- 첫째 줄에 최소 비교 횟수를 출력한다.
"""

# 풀이 제한 시간 : 30분
# 2020/12/03 11:17 ~ 11:34
# 1회 - 출력 초과
# 2회 - 실패

n = int(input())
data = []

for _ in range(n):
    data.append(int(input()))

data.sort()

if len(data) > 1:
    answer = data[0] + data[1]
    sum_value = data[0] + data[1]
    for i in range(2, len(data)):
        sum_value = sum_value + data[i]
        answer += sum_value
else:
    answer = data[0]

print(answer)