"""
외벽 점검
- https://programmers.co.kr/learn/courses/30/lessons/60062
- 레스토랑 내부가 너무 낡아 친구들과 함께 직접 리모델링 하기로 한다.
- 레스토랑이 있는 곳은 스노우타운으로 매우 추운 지역이어서 내부 공사를 하는 도중에 주기적으로 외벽의 상태를 점검해야 할 필요가 있다.
- 레스토랑의 구조는 완전히 동그란 모양이고 외벽의 총 둘레는 n미터이며, 외벽의 몇몇 지점은 추위가 심할 경우 손상될 수도 있는 취약한 지점들이 있다.
- 내부 공사 도중에도 외벽의 취약 지점들이 손상되지 않았는 지, 주기적으로 친구들을 보내서 점검을 하기로 했다.
- 빠른 공사 진행을 위해 점검 시간을 1시간으로 제한한다. 
- 친구들이 1시간 동안 이동할 수 있는 거리는 제각각이기 때문에, 최소한의 친구들을 투입해 취약 지점을 점검하고 나머지 친구들은 내부 공사를 돕도록 하려고 한다.
- 편의 상 레스토랑의 정북 방향 지점을 0으로 나타내며, 취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리로 나타낸다.
- 또, 친구들은 출발 지점부터 시계, 혹은 반시계 방향으로 외벽을 따라서만 이동한다.
- 외벽의 길이 n, 취약 지검의 위치가 담긴 배열 weak, 각 친구가 1시간 종안 이동할 수 있는 거리가 담긴 배열 dist가 매개변수로 주어질 때,
  취약 지점을 점검하기 위해 보내야 하는 친구 수의 최솟값을 return 하는 solution 함수를 완성하시오.

제약 조건
- n은 1 이상 200 이하인 자연수
- weak의 길이는 1 이상 15 이하
- dist의 길이는 1 이상 100 이하인 자연수
- 모든 친구들이 투입되도 취약 지점을 모두 점검할 수 없는 경우 -1을 return
"""

# 2020/11/11 11:44 A.M. ~ 12:44 P.M.
# 실패 - 문제 접근 과정부터 해결책을 떠올리지 못함

from itertools import permutations # 수열 계산 사용을 위한 외부 함수 호출

def solution(n, weak, dist):
    length = len(weak) # 취약 지점의 개수 저장
    # 원형의 벽에 대해서 일자 형태로 취약 지점의 위치를 저장
    for i in range(length):
        weak.append(weak[i]+n) # 예를 들어 n = 12이고 1번이 취약 지점일 경우 13번 취약 지점임을 추가(둘은 같은 취약 지점이다.)
    
    answer = len(dist) + 1 # 투입될 친구의 최솟값을 찾아야 하므로 먼저 최댓값을 설정

    # 취약 지점의 개수 만큼 반복 실행
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수(순열) 각각에 대하여 확인
        # 친구가 m명일 경우 mPm에 대한 모든 경우에 대해서 반복을 진행함
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 특정 취약 지점의 위치와 해당 친구가 움직일 수 있는 거리를 합칠 경우
            # 특정 취약 지점에서 시작하여 해당 친구가 1시간 뒤에 위치할 수 있는 곳(점검할 수 있는 마지막 위치)을 의미
            position = weak[start] + friends[count - 1]

            # 시작점부터 모든 취약 지점을 확인
            # range(start, start + length)를 통해 최대 한 바퀴를 확인 가능함
            for index in range(start, start + length):
                # 취약 지점이 점검 가능한 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1] # 새로 투입된 친구는 다음 취약지점부터 점검 시작

            answer = min(answer, count) # 최솟값 확인

    if answer > len(dist):
        return -1
    else:
        return answer
    

print(solution(12, [1,5,6,10],[1,2,3,4]))
