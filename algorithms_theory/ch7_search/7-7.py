"""
부품 문제 이어서
- 집합 자료형을 이용한 문제 풀이
"""

# N(부품 개수)을 입력받기
n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set)자료형에 기록
array = set(map(int, input().split()))

# M(필요한 부품 종류의 개수)을 입력받기
m = int(input())
# 입력받은 부품의 종류에 대한 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 확인 요청에 필요한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')