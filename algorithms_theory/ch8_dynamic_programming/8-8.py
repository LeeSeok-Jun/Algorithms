"""
효율적인 화폐 구성
- N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 한다.
- 각 화폐 사용의 횟수 제한은 없으며 구성은 같지만 사용 순서가 다른 경우 다른 것으로 간주한다.
- 사용 되는 화폐 개수의 최솟값을 구하여라.

입력 조건
- 첫째 줄에 N, M이 주어진다. (1 <= N <= 100, 1 <= M <= 10,000)
- 이후의 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐의 가치는 10,000보다 작거나 같은 자연수이다.

출력 조건
- 첫째 줄에 경우의 수 X를 출력한다.
- 불가능할 경우 -1를 출력한다.
"""

# 점화식
# 금액 i를 만들 수 있는 최소한의 화폐 개수 a[i], 현재 화폐 단위 k
# a[i-k]를 만드는 방법이 존재하는 경우 a[i] = min(a[i], a[i-k] + 1)
# a[i-k]를 만드는 방법이 존재하지 않는 경우 a[i] = 10,001

# 정수 N, M을 입력받기
n, m = map(int, input().split())

# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
# 먼저 값을 10001로 지정하고 특정 인덱스와 대응되는 화폐 구성이 가능할 경우 그 화폐 구성의 경수의 수로 변경
d = [10001] * (m + 1) # 특정 인덱스에 대응되는 돈을 구성하기 위해 필요한 화폐의 최솟값을 저장

# 보텀업 방식 다이나믹 프로그래밍 진행
d[0] = 0
# n가지의 화폐들에 대해서 반복문 수행
for i in range(n):
    # 현재 화폐 단위부터 목표하는 m까지의 돈을 구성하는 방법을 확인하기 위한 반복문
    for j in range(array[i], m + 1): 
        if d[j - array[i]] != 10001: #(i - k)원을 만드는 방법이 존재하는 경우
            # d[j]의 값은 10,001이거나 이전 단계의 화폐 단위를 통해 계산된 값이 저장되어 있음!
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산 결과 출력
if d[m] == 10001: # 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m]) # 목표햔 m원을 구성하는 최소의 화폐 구성의 수를 출력