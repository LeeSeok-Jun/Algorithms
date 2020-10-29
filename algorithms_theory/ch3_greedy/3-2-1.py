"""
반복되는 수열에 대해서 파악!
- M을 (K+1)로 나눈 몫이 수열이 반복되는 횟수
- 이 곳에 K를 곱하고 나머지를 더하면 가장 큰 수가 더해지는 횟수가 된다.
- int(M / (K + 1)) * K + M % (K + 1)
"""

### 2. 수식을 이용한 답안 ###

# N, M, K를 공백으로 구분하여 입력받기
# map(변환 함수, 순회 데이터) : 여러 순회 가능한 데이터를 한 번에 다른 형태로 변환하기 위해 사용
n, m, k = map(int, input().split()) # 입력받은 값을 공백으로 구분한 후 정수형으로 변환


# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬(오름차수)
first = data[n-1] # 제일 큰 수
secound = data[n-2] # 두 번째 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * secound # 두 번째로 큰 수 더하기


print(result) # 결과