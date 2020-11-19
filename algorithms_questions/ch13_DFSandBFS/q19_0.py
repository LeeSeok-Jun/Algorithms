"""
연산자 끼워 넣기
- https://www.acmicpc.net/problem/14888
- N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램 작성

입력 조건
- 첫째 줄에 수의 개수 N(2 <= N <= 11)이 주어진다.
- 둘째 줄에 Ai ~ An 이 주어진다. (1 <= Ai <= 100)
- 셋째 줄에는 합이 N-1개인 4개의 정수가 주어진다.
    * 차례로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(x)의 개수, 나눗셈(/)의 개수이다.

출력 조건
- 첫째 줄에 만들 수 있는 식의 결과의 최댓값을 출력한다.
- 둘째 줄에는 최솟값을 출력한다.
"""

# 풀이 제한 시간 30분
# 2020/11/19 11:35 A.M. ~ 12:00 P.M.
# 컴파일 시간 초과 -> DFS를 이용하여 해결하시오!

from itertools import permutations # 수열 계산 사용을 위한 외부 함수 호출

n = int(input())

digit = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

oper = []

for _ in range(add):
    oper.append('+')
for _ in range(sub):
    oper.append('-')
for _ in range(mul):
    oper.append('*')
for _ in range(div):
    oper.append('/')

max_value = -1e9 - 1
min_value = 1e9 + 1

candidates = list(permutations(oper, len(oper)))

for candidate in candidates:
    index = 0
    result = digit[index]

    for i in candidate:
        index += 1
        if index >= len(digit):
            break

        if i == '+':
            result += digit[index]
        elif i == '-':
            result -= digit[index]
        elif i == '*':
            result *= digit[index]
        elif i == '/':
            result = int(result / digit[index])

    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)