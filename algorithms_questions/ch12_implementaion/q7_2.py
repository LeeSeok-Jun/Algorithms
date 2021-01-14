"""
럭키 스트레이트 - 3회차
"""

# 풀이 제한 시간 : 20분
# 2021/01/14 12:03 ~ 12:09
# 정답

n = input()

left = n[:int(len(n)/2)]
right = n[int(len(n)/2):]

result = 0
for i in range(len(left)):
    result += int(left[i])
    result -= int(right[i])

if result == 0:
    print("LUCKY")
else:
    print("READY")