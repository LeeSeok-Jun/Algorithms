"""
괄호 변환 - 3회차
"""

# 풀이 제한 시간 : 20분
# 2021/01/19 13:12 ~
# 실패 - 시간초과
# 틀린 부분 주석 처리

def isCorrect(w):
    count = 0
    for i in w:
        if i == "(":
            count += 1
        else:
            count -= 1

            # 이 부분 생각을 못함
            if count == -1:
                return False

    return True

def getBalanceIndex(w):
    count = 0
    for i in range(len(w)):
        if w[i] == '(':
            count += 1
        else:
            count -= 1
        
        if count == 0:
            return i

def solution(p):
    if p == "":
        return ""
    
    bi = getBalanceIndex(p)
    u = p[:bi+1]
    v = p[bi+1:]

    if isCorrect(u):
        # solution(v)
        answer = u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"

        for i in range(1, len(u)-1):
            if u[i] == "(":
                # u[i] = ")"
                answer += ")"
            else:
                # u[i] = "("
                answer += "("

            # answer += u[i]

    return answer

        
