"""
국영수 - 2회차
"""

# 풀이 제한 시간 : 20분
# 2020/12/04 10:55 ~ 11:00
# 로직은 맞는데 코드 채점에서 시간초과 나옴

n = int(input())

data = []

# 이렇게 하면 왜 시간초과?
for _ in range(n):
    name, kor, eng, math = input().split()
    data.append((name, int(kor), int(eng), int(math)))

data.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))


for d in data:
    print(d[0])