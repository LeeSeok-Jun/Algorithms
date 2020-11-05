"""
럭키 스트레이트
- 필살기 '럭키 스트레이트'는 특정 조건에서만 발동된다.
- 현재 캐릭터의 점수가 N이라고 할 때, 
  자리수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자리수의 합과 오른쪽 부분의 각 자리수의 합을 더한 값이 동일한 상황을 말한다.
- 점수 N이 주어지면 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지 알려주는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에 점수 N이 정수로 주어진다. (10 <= N <= 99,999,999)
    * 단, 점수 N의 자리수는 항상 짝수 형태로 주어진다.
    * 예를 들어 12,345와 같은 수는 입력으로 들어오지 않는다.

출력 조건
- 첫째 줄에 럭키 스트레이트를 사용할 수 있다면 "LUCKY"를,
  사용할 수 없다면 "READY"를 출력한다.
"""

# 2020/11/04 03:54 P.M. ~ 03.59 P.M.
# 정답 - https://www.acmicpc.net/problem/18406

n = input()

score = []
for i in n:
    score.append(int(i))

half = int(len(score)/2)

left = sum(score[:half])
right = sum(score[half:])

if left == right:
    print("LUCKY")
else:
    print("READY")