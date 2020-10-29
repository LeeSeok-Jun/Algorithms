"""
시각
- 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하시오.

입력 조건
- 첫째 줄에 정수 N이 입력된다. (0 <= N <= 23)

출력 조건
- 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.
"""

# N을 입력 받기
n = int(input())

count = 0
# 시 단위
for i in range(n + 1): # range n일 경우 (0 ~ n - 1) 이므로 n + 1로 설정
    # 분 단위
    for j in range(60):
        # 초 단위
        for k in range(60):
            # 매 시각 안에 3이 포함되는 경우 count 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)