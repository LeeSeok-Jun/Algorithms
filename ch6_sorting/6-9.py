"""
정렬 라이브러리에서 key를 활용한 소스코드
"""

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting) # 튜플의 리스트에서 갖는 숫자가 낮은 순서대로 정렬
print(result)