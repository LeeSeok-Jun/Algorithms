"""
병사 배치하기
- https://www.acmicpc.net/problem/18353
- 각각 특정한 값의 전투력을 보유하고 있는 N명의 병사가 무작위로 나열되어 있다.
- 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 병사를 배치하고자 한다.
- 즉, 앞에 있는 병사는 뒤에 있는 병사보다 항상 전투력이 높아야 한다.
- 특정 위치의 병사를 제외시키는 방법으로 병사를 배치하는 방법을 이용한다.
- 남아있는 병사 수가 최대로 내림차순으로 정렬되도록 제외 되는 병사의 수를 출력하시오.

입력 조건
- 첫째 줄에 N이 주어진다.
- 둘째 줄에 각 병사의 전투력이 공백으로 구분되어 차례로 주어진다.

출력 조건
- 첫째 줄에 남아있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수를 출력한다.
"""

# 풀이 제한 시간 : 40분
# 2020/12/15 11:28 ~ 12:00
# 실패 - 가장 긴 증가하는 부분 수열 문제 활용하기!

n = int(input())
array = list(map(int, input().split()))
answer= 10e9

def isTopDown(arary):
    length = len(array)

    for i in range(length-1):
        for j in range(i+1, length):
            if array[i] < array[j]:
                return False

    return True

def topDown(array):
    global answer

    if isTopDown(array):
        answer = min(answer, n-len(array))

    else:
        pass
