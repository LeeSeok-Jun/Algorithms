"""
곱하기 혹은 더하기 - 3회차
"""

# 풀이 제한 시간 : 30분
# 2021/01/13 13:38 ~

s = input()
data = []
for i in s:
    data.append(int(i))

result = data[0]
for i in range(1, len(data)):
    if result == 0 or data[i] <= 1:
        result += data[i]
    else:
        result *= data[i]

print(result)
    