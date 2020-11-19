"""
연산자 끼워 넣기 - 해설
"""

n = int(input())

digit = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

max_value = -1e9
min_value = 1e9

# DFS
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    # 모든 연산자 사용한 경우 최소 최댓값 갱신
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        # 각 연산자에 대해 재귀적 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + digit[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - digit[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * digit[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / digit[i]))
            div += 1

dfs(1, digit[0])

print(max_value)
print(min_value)