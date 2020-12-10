"""
공유기 설치 - 2회차
"""

# 풀이 제한 시간 : 50분
# 2020/12/10 11:02 ~ 11:13
# 적절한 부등호 사용 실패!

n, c = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort()

min_gap = 1
max_gap = array[n-1] - array[0]

answer = 0

# 부등호 (<=) 주의!
while(min_gap <= max_gap):
    mid = (min_gap + max_gap) // 2
    count = 1
    installed = array[0]

    for i in range(1, n):
        # 부등호 (<=) 주의!
        if array[i] >= installed + mid:
            count += 1
            installed = array[i]

    if count >= c:
        min_gap = mid + 1
        answer = mid
    
    else:
        max_gap = mid - 1

print(answer)