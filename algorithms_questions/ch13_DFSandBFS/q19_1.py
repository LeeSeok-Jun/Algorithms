"""
연산자 끼워 넣기 - 2회차
"""

# 풀이 제한 시간 : 30분
# 2020/11/27 11:40 ~ 12:01
# 실패 - 연산자들에 대해서 if-else 가 아니라 각각 if로 실행시켜야 한다!

n = int(input())

digits = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

max_result = -1e9
min_result = 1e9

def oper(result, index):
    global max_result, min_result, add, sub, mul, div

    if index < n:
        if add > 0:
            add -= 1
            oper(result + digits[index], index + 1)
            add += 1
        # elif sub > 0:
        if sub > 0:
            sub -= 1
            oper(result - digits[index], index + 1)
            sub += 1
        # elif mul > 0:
        if mul > 0:
            mul -= 1
            oper(result * digits[index], index + 1)
            mul += 1
        # elif div > 0:
        if div > 0:
            div -= 1
            oper(int(result / digits[index]), index + 1)
            div += 1
    
    else:
        min_result = min(min_result, result)
        max_result = max(max_result, result)

oper(digits[0], 1)

print(max_result)
print(min_result)