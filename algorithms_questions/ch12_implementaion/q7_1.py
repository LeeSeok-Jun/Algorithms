"""
럭키 스트레이트 - 2회차
"""

# 2020/11/12 10:50 A.M. ~ 10:54 A.M.
# 정답

n = input()

data = []
for i in n:
    data.append(int(i))

left = sum(data[:int(len(data)/2)])
right = sum(data[int(len(data)/2):])

if left - right == 0:
    print("LUCKY")
else:
    print("READY")