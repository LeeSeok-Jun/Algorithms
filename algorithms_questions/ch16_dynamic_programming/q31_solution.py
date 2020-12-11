"""
금광 - 문제 풀이
"""

for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    # 1차원 배열을 한 행의 길이가 m인 2차원 배열로 변환
    for i in range(n):
        dp.append(array[index:index+m])
        index += m

    # 다이나믹 프로그래밍 진행
    # 점화식 : dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
    for j in range(1, m): # 열
        for i in range(n): # 행
            # 왼쪽 위에서부터 채굴
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            
            # 왼쪽 아래서부터 채굴
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            # 왼쪽에서부터 채굴
            left = dp[i][j-1]

            # 점화식에 대입하여 현재의 최대값을 DP 테이블에 저장
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)

    
    result = 0
    # DP 테이블의 마지막 열에서 나올 수 있는 최댓값을 저장
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)