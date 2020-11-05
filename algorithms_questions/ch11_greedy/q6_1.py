"""
무지의 먹방 라이브 - 2회차
"""

# 2020/11/04 02:55 P.M. ~ 03:47 P.M.
# 풀이 최대한 이해해보기

import heapq

def solution(food_times, k):
    # 전체 음식을 방송 시작후 k초 이전에 다 먹는 경우 -1 반환
    if sum(food_times) <= k:
        return -1

    # 시간이 적은 음식 부터 섭취(우선순위 큐 이용)
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호)의 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1)) # 음식 번호 = 인덱스 + 1

    # 먼저, 우선순위 큐에 있는 가장 시간이 적은 음식을 다 먹는데 걸리는 시간이 n초라고 가정한다.
    # (n * 남은 음식의 개수)가 k보다 작을 경우, 해당 음식은 k초 전에 다 먹을 수 있다.
    # 그리고 다른 음식들은 남은 시간이 (n * 남은 음식의 개수)만큼 줄어든다.
    # 남은 음식들 중 가장 먹는데 시간이 적은 음식에 대해 위 과정을 반복한다.
    # 반복하다가 지금까지 누적된 남은 음식을 다 먹는데 걸리는 시간이 k를 넘어가는 것으로 예측되면 반복을 멈춘다.

    sum_value = 0 # 음식을 먹기 위해 사용된 누적 시간
    previous = 0 # 이전에 소요시간이 가장 짧은 음식을 다 먹기 위해 소요된 시간
    length = len(food_times) # 남은 음식의 총 갯수

    # q[0][0] : 우선순위 큐에서 섭취 시간이 가장 작은 음식의 남은 섭취 시간
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0] # 우선순위 큐에서 음식을 꺼내고 음식의 남은 섭취시간 저장

        sum_value += (now - previous) * length # 지금까지 음식을 먹는데 걸린 누적시간 저장
        # 위 과정에서 하나의 음식은 다 먹은 것으로 처리가 된다.

        length -= 1 # 남은 음식의 개수를 줄임
        previous = now # 음식을 다 먹었으므로 이전에 음식을 다 섭취하는데 소요된 시간으로 새롭게 설정

    # 이제 남은 음식들 중 몇 번째 음식을 먹어야 되는지 확인
    result = sorted(q, key = lambda x: x[1]) # 음식 번호를 기준으로 정렬
    # 현재 result에 이미 음식을 다 먹은 것들은 삭제되어있다.
    # reuslt = [(음식 시간, 음식 번호), ...]
    return result[(k - sum_value) % length][1]

food_times = [8, 6, 4]
k = 15
print(solution(food_times, k))