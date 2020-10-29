"""
커리큘럼
- 어떤 학생이 온라인으로 강의를 듣고 있으며 어떤 강의는 선수 강의를 들어야만 수강이 가능하다.
- 학생이 총 N개의 강의를 듣고자 한다. 모든 강의는 1번부터 N번까지의 번호를 가지며 동시에 여러 강의를 들을 수 있다.
- 학생이 듣고자 하는 N개의 강의 정보가 주어졌을 때, N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각각 출력하는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에 학생이 듣고자 하는 강의의 수(1 <= N <= 500)이 주어진다.
- 다음 N개의 줄에는 각 강의의 강의 시간과 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호가 자연수로 주어지며,
  각 자연수는 공백으로 구분한다. 이때 강의 시간은 100,000 이하의 자연수이다.
- 각 강의 번호는 1부터 N까지로 구성되며, 각 줄은 -1로 끝난다.

출력 조건
- N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력한다.
"""

from collections import deque # 큐를 구현하기 위한 라이브러리
import copy # 리스트 값 복사를 위한 라이브러리

# 노드의 개수 입력
v = int(input())

# 모든 노드의 진입차수는 0으로 초기화
indegree = [0] * (v + 1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]

# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    # data[0] : 강의 시간 정보
    # data[1:-1] : 선수 강의 번호
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1 # 선수 과목이 존재하는 경우 진입 차수 증가
        graph[x].append(i) # x번 그래프에는 i가 연결되어 있음을 저장

# 위상 정렬 알고리즘
def topology_sort():
    # result에 특정 인덱스에 상응하는 강의를 수강하기 까지 누적된 최소 시간을 담는다.
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수를 1씩 감소
        for i in graph[now]:
            # 인접한 노드에 대해서 강의 시간이 더 오래 걸리는 값으로 변경
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v + 1):
        print(result[i])

topology_sort()