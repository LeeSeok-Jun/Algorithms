"""
1이 될 때까지 이어서
"""

### 2. 효율적인 답안 ###

# N, K를 공백으로 입력받아 확인
n, k = map(int, input().split())
result = 0

while True:
    # 변수 n이 K의 배수가 되는 수 까지 N에서 1씩 빼서 그 배수가 되는 값을 저장
    target = (n // k) * k
    result += (n - target) # 변수 n에서 K의 배수가 되는 수까지 빼기를 진행하고 그 횟수를 증가

    # 나눗셈 진행
    n = target
    # 변수 n이 K보다 작을 때 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

result += (n - 1) # 마지막으로 남은 n에 대하여 n이 1이 될때까지 빼는 횟수(n-1) 더하기
print(result) # 결과 출력