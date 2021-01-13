"""
문자열 뒤집기 - 3회차
"""

# 풀이 제한 시간 : 20분
# 2021/01/13 13:44 ~ 14:00
# 틀림

s = input()

flip_to_one = 0
flip_to_zero = 0

# 빼먹은 부분
if s[0] == '0':
    flip_to_one += 1
else:
    flip_to_zero += 1

# 범위는 0부터 탐색해야 한다.
# for i in range(1, len(s) - 1) -> 틀림
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            flip_to_one += 1
        else:
            flip_to_zero += 1

print(min(flip_to_one, flip_to_zero))