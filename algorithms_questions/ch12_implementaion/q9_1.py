"""
문자열 압축 - 2회차
"""

# 2020/11/12 11:05 A.M. ~ 11:25 A.M.
# 정답


def solution(s):
    answer = 1001

    for iter in range(1, len(s)+1):
        i = 0
        count = 1
        temp = ""

        while(i <= len(s)):

            if s[i:i+iter] == s[i+iter:i+(2*iter)]:
                count += 1
            else:
                if count <= 1:
                    temp += s[i:i+iter]
                else:
                    temp += str(count) + s[i:i+iter]
                
                count = 1

            i += iter

        answer = min(answer, len(temp))

    return answer

print(solution("xababcdcdababcdcd"))