"""
문자열 압축 - 3회차
"""

# 풀이 제한 시간 : 30분
# 2021/01/14 12:25 ~ 13:05
# 실패 - 시간 초과 (알고리즘은 정답)

def solution(s):
    n = len(s)
    answer = ""
    count = 1
    min_value = 1001
    
    for i in range(1, n+1):
        j = 0

        while j < n:
            if s[j:j+i] == s[j+i:j+2*i]:
                count += 1
            else:
                if count != 1:
                    answer += str(count) + s[j:j+i]
                    count = 1
                else:
                    answer += s[j:j+i]

            j += i

        min_value = min(min_value, len(answer))
        answer = ""

    return min_value

print(solution("abcabcdede"))