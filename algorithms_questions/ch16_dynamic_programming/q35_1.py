"""
못생긴 수 - 2회차
"""

# 풀이 제한 시간 : 30분
# 2020/12/17 10:15 ~ 10:28
# 성공

n = int(input())
array = [0] * n
array[0] = 1

next2, next3, next5 = 2, 3, 5
i2 = i3 = i5 = 0

for i in range(1, n):
    next = min(next2, next3, next5)
    array[i] = next

    if next == next2:
        i2 += 1
        next2 = array[i2] * 2
    
    if next == next3:
        i3 += 1
        next3 = array[i3] * 3

    if next == next5:
        i5 += 1
        next5 = array[i5] * 5

    

print(array[n-1])