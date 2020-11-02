"""
무지의 먹방 라이브
- 회전판에는 먹방 방송인 무지가 먹어야 할 N개의 음식이 있다.
- 각 음식에는 1부터 N까지의 번호가 붙어있으며, 각 음식을 섭취하는데 일정 시간이 소요된다.
- 무지는 다음과 같은 방법으로 음식을 섭취한다.
    1. 무지는 1번 음식부터 먹기 시작하여, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓는다.
    2. 마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 온다.
    3. 무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취한다.
       다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식을 말한다.
    4. 회전판이 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없다고 가정한다.
- 무지가 음식을 먹기 시작한 후 K초 후에 네트워크 장애로 잠시 먹방이 중지되었다.
- 무지는 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지 알고자 한다.
- 각 음식을 모두 먹는 데 필요한 시간이 담겨 있는 배열 food_times,
  네트워크 장애가 발생한 시간 K초가 매개변수로 주어질 때 몇 번음식부터 다시 섭취하면 되는지 return하도록 solution 함수를 완성하라.

제한 사항
- food_times는 각 음식을 모두 먹는 데 필요한 시간이 음식의 번호 순서대로 들어 있는 배열이다.
- k는 방송이 중단된 시간을 나타낸다.
- 만약 더 섭취해야 할 음식이 없다면 -1을 반환한다.
"""

# 2020/11/02 04:10 P.M ~ 04:31 P.M
# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3
# 정답 해설과 접근 과정이 다름
# 정확성 : 25.4 / 효율성 : 0.0

### 내가 생각한 풀이 방법 ###

def solution(k):
    # 배열 입력
    food_times = list(map(int, input().split()))
    longest = food_times.index(max(food_times))
    now = 0
    i = 0

    while(now < k):
        if food_times[i] == 0:
            i += 1
            if i >= len(food_times):
                i = 0
            continue
        food_times[i] -= 1
        now += 1
        i += 1
        if i >= len(food_times):
            i = 0
        elif food_times[longest] == 0 and now < k:
            return -1

    return i
    
print("장애 복구 후", solution(5) + 1, "번 음식부터 다시 먹기 시작하면 됩니다.")

### 정답 해설 방법 ###

import heapq

def muzi_solution(food_times, k):
    # 전체 음식을 먹는 시간 보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 적은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹음 음식 시간

    length = len(food_times) # 남은 음식의 개수

    # {sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수} 와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]
