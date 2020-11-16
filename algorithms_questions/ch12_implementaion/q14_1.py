"""
외벽 점검 - 2회차
"""

# 2020/11/16 01:23 P.M. ~
# 실패

from itertools import permutations # 수열 계산 사용을 위한 외부 함수 호출

def solution(n, weak, dist):
    answer = len(dist)+1
    num_of_weak = len(weak) # 취약 지점의 수

    for i in range(num_of_weak):
        weak.append(weak[i]+n)
    
    for start in range(num_of_weak):

        for friends in list(permutations(dist, len(dist))):
            
            count = 1
            last_position = weak[start] + friends[count - 1] # 처음 투입되는 친구의 1시간 뒤 위치
            
            for index in range(start, start+num_of_weak): # 한 바퀴 확인
                # 1시간 뒤 남은 점검하지 못한 취약지점이 남아있는 경우
                if last_position < weak[index]:
                    count += 1 # 추가 투입
                    if count > len(dist):
                        break
                    # 남은 취약지점부터 새롭게 점검
                    last_position = weak[index] + friends[count - 1]

            answer = min(answer, count)

    if answer > len(dist):
        return -1
    else:
        return answer