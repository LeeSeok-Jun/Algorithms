"""
문자열 재정렬 - 2회차
"""

# 2020/11/12 10:55 A.M. ~ 11:04 A.M.
# 정답

s = input()

alpha = []
digit = []

for i in s:
    if ord(i) >= 48 and ord(i) <= 57:
        digit.append(int(i))
    else:
        alpha.append(i)

alpha.sort()

if len(digit) > 0:
    print(''.join(alpha) + str(sum(digit)))
else:
    print(''.join(alpha))