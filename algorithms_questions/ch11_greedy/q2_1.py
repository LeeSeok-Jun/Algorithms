"""
곱하기 혹은 더하기 - 2회차
"""

# 2020/11/03 03:20 P.M. ~ 03:26 P.M.
# 정답

s = input()

data = []
for i in s:
    data.append(int(i))

result = data[0]

for i in range(1, len(data)):
    if data[i] == 0 or data[i] == 1 or result <= 1:
        result += data[i]
    else:
        result *= data[i]

print(result)