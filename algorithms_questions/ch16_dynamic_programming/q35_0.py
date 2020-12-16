"""
못생긴 수
- 못생긴 수란 2, 3, 5만을 소인수로 가지는 수를 의미한다.
- 1 역시 못생긴 수라고 가정한다.
- n번째 못생긴 수를 찾는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에 n이 입력된다.

출력 조건
- n번째 못생긴 수를 출력한다.
"""

# 풀이 제한 시간 : 30
# 2020/12/15 12:15 ~ 12:25
# 실패 - 다이나믹 프로그래밍 방식으로 구현하지 않음

n = int(input())

array = [1]
index = 0

while True:
    if len(array) >= 2*n:
        break

    ugly = [2, 3, 5]
    
    for u in ugly:
        if array[index] * u not in array:
            array.append(array[index] * u)

    index += 1

array.sort()
print(array[n-1])