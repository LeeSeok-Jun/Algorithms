"""
파이썬 라이브러리에서의 정렬
"""

# 1. sorted()
# 최악의 경우에도 O(NlogN) : 퀵 정렬과 비슷한 병합 정렬을 기반으로 함
# 새로운 리스트를 반환

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

# 2. sort()
# 새로운 리스트의 반환 없이 리스트의 내부 원소가 바로 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()
print(array)

# 3. key를 활용한 정렬

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

# 방법 1
def setting(data):
    return data[1]

result = sorted(array, key=setting)

# 방법 2
result = sorted(array, key=lambda data: data[1])

print(result)