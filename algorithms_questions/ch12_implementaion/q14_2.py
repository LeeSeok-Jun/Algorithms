"""
외벽 점검 - 3회차
"""

# 풀이 제한 시간 : 50분
# 2021/01/18 13:22 ~ 13:55
# 실패 - 코드 꼼꼼하게 분석하고 문제 해결방법 이해하기!

from itertools import permutations # 문제 해결을 위한 수열 라이브러리 사용

# n = 외벽 길이
# weak = 취약지점의 수와 위치
# dist = 친구들의 수와 1시간 당 이동가능 거리
def solution(n, weak, dist):
    # 최종 결과값은 친구들의 수를 넘어갈 수 없음
    # 친구들의 수 + 1인 len(dist) + 1를 임시로 최댓값으로 설정 
    answer = len(dist) + 1
    num_of_weak = len(weak) # 취약지점의 수

    # 한 바퀴를 완전히 도는 경우도 있으므로 한 바퀴 돌았을 때 취약지점의 위치를 가정함
    for i in range(num_of_weak):
        weak.append(weak[i] + n) # 한 바퀴 돈 이후의 취약지점의 위치 추가
        # 취약지점의 수는 기존의 2배가 된다.

    # 외벽 점검 시작
    for start in range(num_of_weak):

        # 친구들의 수 만큼 친구들의 시간 당 이동 거리를 수열을 통해 정렬
        for friends in list(permutations(dist, len(dist))):

            count += 1 # 현재 외벽 점검 중인 친구의 수
            # 처음 외벽 점검을 나간 친구의 1시간 뒤 위치
            last_position = weak[start] + friends[count - 1]

            # 한 바퀴 확인하기
            for index in range(start, start+num_of_weak):
                # 1시간 뒤에 점검하지 못한 취약지점이 남아있는 경우
                if last_position < weak[index]:
                    count += 1 # 추가 투입

                    if count > len(dist):
                        break # 추가 투입 인원이 친구들의 수 보다 큰 경우 점검 불가능
                    
                    # 남은 취약지점부터 새롭게 점검 시작
                    last_position = weak[index] + friends[count - 1]
        
        answer = min(answer, count)

    if answer > len(dist):
        return -1
    else:
        return answer