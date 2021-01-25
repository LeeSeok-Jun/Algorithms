"""
못생긴 수 - 3회차
"""

# 풀이 제한 시간 : 30분
# 2021/01/25 15:15 ~ 15:44
# 실패

n = int(input())

"""
ugly = [1]

next = [2, 3, 5]

for i in range(n+1):
    for j in range(3):
        next[j] = ugly[i] * next[j]
    print("next : ", next)

    ugly.append(min(next))
    print("ugly : ", ugly)

print(ugly[n-1])
"""

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    ugly.append(min(next2, next3, next5))

    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2] * 2

    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3] * 3

    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n-1])