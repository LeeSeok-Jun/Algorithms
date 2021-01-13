"""
무지의 먹방 라이브 - 3회차
"""

# 풀이 제한 시간 : 30분
# 2021/01/13 14:40 ~ 15:07
# 실패

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    # 음식 정보를 우선순위 큐에 저장
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    sum_value = 0 # 음식 섭취 누적 시간
    previous = 0 # 이전에 소요시간이 가장 적은 음식의 총 섭취 소요 시간
    length = len(food_times) # 남은 음식의 개수

    # 누적 시간 + 다음 음식 다 먹는데 걸리는 시간이 k보다 작으면 다음 반복을 진행
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0] # 현재 음식의 남은 소요시간

        sum_value += (now - previous) * length

        length -= 1
        previous = now

    result = sorted(q, key = lambda x : x[1]) # 음식 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]

