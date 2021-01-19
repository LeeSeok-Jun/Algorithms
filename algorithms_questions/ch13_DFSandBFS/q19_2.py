"""
연산자 끼워 넣기 - 3회차
"""

# 풀이 제한 시간 : 30분
# 2021/01:19 13:44 ~
# 실패 - 풀이 방법을 구현하지 못함... 코드 꼼꼼하게 분석하고 이해하기!

n = int(input())
data = list(map(int, input().split()))
a, s, m, d = map(int, input().split())

max_value = -int(1e9)
min_value = int(1e9)

# 내가 생각하지 못한 부분
def getAnswer(result, index):
    # 전역 변수로 설정
    global max_value, min_value, a, s, m, d

    # 모든 경우에 대해 재귀적으로 연산 진행
    if index < n:
        if a > 0:
            a -= 1
            getAnswer(result + data[index], index + 1)
            a += 1

        if s > 0:
            s -= 1
            getAnswer(result - data[index], index + 1)
            s += 1

        if m > 0:
            m -= 1
            getAnswer(result * data[index], index + 1)
            m += 1

        if d > 0:
            d -= 1
            getAnswer(int(result / data[index]), index + 1)
            d += 1

    # 모든 수열에 대해 계산이 끝난경우 최솟값, 최댓값을 갱신
    else:
        min_value = min(min_value, result)
        max_value = max(max_value, result)

getAnswer(data[0], 1)

print(max_value)
print(min_value)