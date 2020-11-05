"""
문자열 압축
- https://programmers.co.kr/learn/courses/30/lessons/60057
- 압축할 문자열 s가 매개변수로 주어질 때, 1개 이상 단위로 문자열을 잘라 압축표현한 문자열 중 가장 짧은 것의 길이를 return하는 solution 함수를 완성하시오.
"""

# 2020/11/05 02:40 P.M. ~ 03:20 P.M.
# 실패 - 풀이 시간 초과
# 채점 결과 : 96.0 /100.0

# 첫 반복문의 범위를 range(1, len(s))에서 range(1, len(s)+1)로 바꿔야 함
# 채점 결과 : 100.0 / 100.0


def solution(s):
    answer = 1001 # 최대 문자열의 길이는 1000

    # for i in range(1, len(s)): -> 틀린 이유
    # 여기서 i는 문자열을 자르는 단위(일종의 step)
    for i in range(1, len(s)+1):
        result = '' # 압축될 문자열이 들어갈 변수
        count = 1 # 중복된 문자열이 등장할 시 중복 횟수를 저장할 변수
        j = 0 # 문자열에서 현재 탐색하고 있는 인덱스의 값

        # 인덱스가 문자열의 길이를 벗어날때 까지 반복 진행
        while(True):
            if j > len(s):
                break
            
            # 문자열의 j구간부터 j+i이전의 구간과 j+i 부터 j+2*i까지의 문자열이 같다면 count 증가
            if s[j : j+i] == s[j+i : j+2*i]:
                count += 1
            # 특정 구간의 문자열이 서로 달라지면 문자열 압축 표현 진행
            else:
                if count != 1:
                    result += str(count) + s[j : j+i]
                else:
                    result += s[j : j+i]

                count = 1 # 중복 횟수 초기화
            
            j += i # 다음 구간부터 새롭게 문자열 비교 시작

        # 특정 step에 대한 압축이 끝날 경우 기존의 길이와 비교하여 answer를 초기화 
        if len(result) < answer:
            answer = len(result)
        

    return answer

print(solution('xababcdcdababcdcd'))