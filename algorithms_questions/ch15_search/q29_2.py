"""
공유기 설치 - 3회차
"""

# 풀이 제한 시간 : 50분
# 2021/01/22 13:40 ~ 14:12
# 실패 - 틀린 부분 주석 처리
# 이진 탐색을 응용하여 푸는 방법이 필요함

n, c = map(int, input().split())

data = []
for _ in range(n):
    data.append(int(input()))

data.sort()

# min_distance = len(data)
# answer = 0

# now_installed_index = 0
# installed = 1

"""
# 첫 번째 생각
for i in range(1, len(data)):
    next_installed = now_installed + i
    installed += 1

    if next_installed < len(data) and installed <= 3:
        now_installed = next_installed
        min_distance = min(min_distance, data[next_installed] - data[now_installed])

    answer = max(min_distance, answer)

print(answer)
"""

"""
# 두 번째 생각
i = 1
while installed <= 3:
    if i >= len(data):
        break

    next_installed_index = now_installed_index + i
    installed += 1

    if next_installed_index >= len(data):
        continue

    min_distance = min(min_distance, data[next_installed_index] - data[now_installed_index])
    now_installed_index = next_installed_index

    answer = max(answer, min_distance)
    i += 1

print(answer)
"""

min_gap = 1 # 공유기가 설치될 수 있는 최소 거리
max_gap = data[n-1] - data[0] # 공유기가 설치 될 수 있는 최대 거리

answer = 0

while(min_gap <= max_gap):
    mid = (min_gap + max_gap) // 2 # 공유기가 설치될 임의의 거리차 설정
    installed = data[0] # 현재 공유기가 설치된 집의 위치
    count = 1 # 공유기 설치 수

    # 다른 집들에 대해
    for i in range(1, n):
        # 다음 집의 위치가 임의의 거리 차보다 멀리 위치 한 경우
        if data[i] >= installed + mid:
            installed = data[i] # 해당 집에 공유기 설치
            count += 1

    # 설치된 공유기의 수가 문제에서 입력된 수 보다 큰 경우
    # 최소 간격을 더 늘려서 공유기를 설치할 수 있다.
    if count >= c:
        min_gap = mid + 1
        answer = mid # 최종적으로 최소 간격의 최댓값을 저장하게 된다.

    # 설치된 공유기의 수가 문제에서 입력된 수 보다 적은 경우
    # 최대 간격을 줄여서 공유기를 다시 설치해본다.
    else:
        max_gap = mid - 1

print(answer)