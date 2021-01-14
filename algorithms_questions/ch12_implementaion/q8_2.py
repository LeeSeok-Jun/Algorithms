"""
문자열 재정렬 - 3회차
"""

# 풀이 제한 시간 : 20분
# 2021/01/14 12:11 ~ 12:21
# 정답 - 배열을 문자열로 출력하는 방법에 대해서 join함수를 사용하자!

s = input()

sum_value = 0
data = []
for c in s:
    if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        sum_value += int(c)
    else:
        data.append(c)

data.sort()

"""
# 내가 푼 방법
if sum_value != 0:
    data.append(sum_value)

for d in data:
    print(d, end='')
"""

# 풀이에서 제시하는 방법
if sum_value != 0:
    data.append(str(sum_value))
print(''.join(data))