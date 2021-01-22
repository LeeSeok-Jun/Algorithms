"""
순차 탐색
- 최약의 경우 시간 복잡도 O(N)
"""

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i

