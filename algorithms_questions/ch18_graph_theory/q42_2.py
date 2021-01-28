"""
탑승구 - 3회차
"""

# 풀이 제한 시간 : 50분
# 2021/01/27 14:22 ~ 14:34
# 입력 예시들에 대한 답은 맞았으나 풀이 방법과 비교하면 다른 부분이 존재, 맞는 방법인지는 모르겠음.

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


g = int(input())
p = int(input())

plane = []
for i in range(p):
    plane.append(int(input()))

parent = [0] * (g + 1)
for i in range(g+1):
    parent[i] = i

answer = 0
# 내가 생각한 방법
# for pl in plane:
#     if find_parent(parent, pl) != find_parent(parent, pl - 1):
#         union_parent(parent, pl, pl - 1)
#         answer += 1

# 해설에서 제시한 방법
for pl in plane:
    if find_parent(parent, pl) == 0:
        break
    
    union_parent(parent, pl, pl-1)
    answer += 1

print(answer)