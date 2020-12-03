"""
실패율
- https://programmers.co.kr/learn/courses/30/lessons/42889
- 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
"""

# 풀이 제한 시간 : 20분
# 2020/12/03 10:52 ~ 11:08
# 실패 - 70.4 /100

def solution(N, stages):
    num_user = len(stages)
    data = []
    answer = []

    for i in range(1, N+1):
        num = 0
        failure = 0
        for stage in stages:
            if stage == i:
                num += 1

        ### 해당 부분으로 고치면 정답#####
        if num_user <= 0:
            failure = 0
        else:
            failure = num / num_user
        ################################

        data.append((i, failure))

        num_user -= num

        # 내가 틀린 부분
        """
        if num_user <= 0:
            break
        """

    data.sort(key= lambda x : (-x[1], x[0]))

    for i in data:
        answer.append(i[0])

    return answer

print(solution(4, [4,4,4,4,4]))