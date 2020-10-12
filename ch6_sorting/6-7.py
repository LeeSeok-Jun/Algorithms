"""
파이썬 라이브러리 sorted()
- 퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만듦.
- 최악의 경우에도 시간복잡도 O(NlogN)을 보장
- 새로운 리스트를 반환
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)