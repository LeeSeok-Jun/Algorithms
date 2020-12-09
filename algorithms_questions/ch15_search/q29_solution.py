"""
공유기 설치 - 문제 해설
"""

n, c = map(int, input().split())

data = []
for _ in range(n):
    data.append(int(input()))

data.sort()

min_gap = 1 # 공유기가 설치될 수 있는 인접한 두 집 사이 거리의 최소값
max_gap = data[n-1] - data[0] # 공유기가 설치될 수 있는 인접한 두 집 사이 거리의 최대값

answer = 0

while (min_gap <= max_gap):
    mid = (min_gap + max_gap) // 2 # 임의의 공유기가 설치될 인접한 두 집간의 거리
    installed = data[0] # 공유기가 설치 된 집(첫번째 집부터 설치한다고 가정함)
    count = 1 # 현개 공유기의 설치 수

    for i in range(1, n): # 다른 집들에 대해서
        if data[i] >= installed + mid: # 임의의 거리 차보다 두 집 사이의 거리가 먼 경우
            installed = data[i] # 해당 집에 공유기를 설치
            count += 1 # 설치된 공유기의 개수 추가

    # 설치된 공유기의 개수가 c보다 큰 경우 -> 최소 간격을 더 늘려서 공유기 설치
    if count >= c: 
        min_gap = mid + 1
        answer = mid # 최종적으로 최소 간격의 최댓값을 저장
    # 설치된 공유기의 개수가 c보다 작은 경우 -> 최대 간격을 더 줄여서 공유기 설치
    else:
        max_gap = mid - 1

print(answer)