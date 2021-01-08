"""
큐(Queue)
- First In, First Out
- collections 패키지의 deque를 통해 구현
- 삽입 : append(element)
- 추출 : popleft()
"""

from collections import deque

queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 좌에서 우로 출력

queue.reverse()
print(queue) # 나중에 들어온 순서대로 출력

"""
우선순위 큐(Priority Queue)와 힙(Heap)

힙(Heap)
- 완전 이진 트리의 일종으로 우선순위 큐를 위한 자료구조
- 느슨한 정렬 상태를 유지함
    * 최대 힙(max heap) : 부모 노드의 키 값이 항상 자식 노드의 키 값보다 크거나 같은 완전 이진 트리
    * 최소 힙(min heap) : 부모 노드의 키 값이 항상 자식 노드의 키 값보다 작거나 같은 완전 이진 트리
- 파이썬 라이브러리 hepq은 최소 힙을 지원한다.
"""

import heapq # 우선순위 큐를 구현하기 위한 최소 힙 호출

# 초기화
q = []

# 원소 삽입
# q에 (비용, 번호)인 노드를 삽입하는 예시
heapq.heappush(q, (0, 1))
print(q)
heapq.heappush(q, (3, 2))
print(q)
heapq.heappush(q, (2, 3))
print(q)

# 원소 추출
# q에서 차례대로 원소 추출하는 예시
# q에서는 비용이 작은 순서대로 차례로 빠져 나온다.(최소 힙)
heapq.heappop(q)
print(q)
heapq.heappop(q)
print(q)
heapq.heappop(q)
print(q)