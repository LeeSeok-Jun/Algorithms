"""
문자열 재정렬
- 알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어진다.
- 모든 알파벳을 오름차순으로 정렬하고 그 뒤로 모든 숫자를 더한 값을 이어서 출력한다.

입력 조건
- 첫째 줄에 하나의 문자열 S가 주어진다. (1 <= S의 길이 <= 10,000)

출력 조건
- 첫째 줄에 문제에서 요구하는 정답을 출력한다.
"""

# 2020/11/04 04:08 P.M ~ 04:14 P.M.
# 문자열에 숫자가 없는 경우도 가정해야 함

s = input()

alpha = []
digit = []

for i in s:
    if ord(i) >= 48 and ord(i) <= 57:
        digit.append(int(i))
    else:
        alpha.append(i)

alpha.sort()

# print(''.join(alpha) + str(sum(digit)))

if len(digit) > 0:
    print(''.join(alpha) + str(sum(digit)))
else:
    print(''.join(alpha))