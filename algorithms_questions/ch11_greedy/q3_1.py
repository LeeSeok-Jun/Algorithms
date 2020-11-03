"""
문자열 뒤집기 - 2회차
"""

# 2020/11/03 03:28 P.M. ~ 03:31 P.M.
# 정답

s = input()

flip_to_one = 0
flip_to_zero = 0

if s[0] == '0':
    flip_to_one += 1
else:
    flip_to_zero += 1

for i in range(1, len(s) - 1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            flip_to_one += 1
        else:
            flip_to_zero += 1

print(min(flip_to_one, flip_to_zero))