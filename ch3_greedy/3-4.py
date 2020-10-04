"""
숫자 카드 게임 이어서
"""

### 2. 2중 반복문 구조를 이용한 답안 ###

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 행에서 가장 작은 수를 찾기
    min_value = 10001 # 임의의 큰 수 적용(최대 10,000이므로 10,001로 설정)
    for a in data:
        min_value = min(min_value, a)
    
    # 다른 행의 작은 값들을 비교 후 그 중 최댓값 저장
    result = max(result, min_value)

print(result) # 결과 출력
