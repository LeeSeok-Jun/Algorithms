"""
못생긴 수 - 문제 해설
"""

n = int(input())

ugly = [0] * n
ugly[0] = 1

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음에 곱셈값을 초기화
next2, next3, next5 = 2, 3, 5

# 1부터 n까지의 못생긴 수 찾기
for l in range(1, n):
    # print('i :', i2, i3, i5)
    # print('next : ', next2, next3, next5)

    # 가능한 곱셈 결과 중 가장 작은 수를 선택
    ugly[l] = min(next2, next3, next5)

    # 인덱스에 따라서 곱셈 결과를 증가
    # next 값들이 동일한 경우도 있으므로 if-elif 가 아니라 if-if로 따로 묶는다. 
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2

    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3

    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5
    

print(ugly[n-1])