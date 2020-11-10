"""
치킨 배달
-https://www.acmicpc.net/problem/15686
- 1 * 1 크기의 칸으로 나누어진 N * N 크기의 도시가 있다.
- 도시의 각 칸은 빈 칸, 치킨집, 일반 가정집 중 하나이다.
- 도시의 칸은 (행, 열)로 표현되는 (r, c)와 같은 형태로 나타나고 r과 c는 1부터 시작한다.
- 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다.
    * 집을 기준으로 정해지며 각각의 집은 치킨 거리를 가지고 있다.
    * 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
- 임의의 두 칸 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.
- 도시에 있는 치킨집 중에서 최대 M개를 골라 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에 N(2 <= N <= 50)과 M(1 <= M <= 13)이 주어진다.
- 둘째 줄 부터 N개의 줄에는 도시의 정보가 주어진다.
- 도시의 정보는 0,1,2로 이루어져 있다.
    * 0은 빈칸, 1은 집, 2는 치킨집이다.
    * 집의 개수는 2N개를 넘지 않으며 적어도 1개 이상 존재한다.
    * 치킨집의 개수는 M보다 크거나 같고 13보다 작거나 같다.

출력 조건
- 첫째 줄에 폐업시키지 않을 치킨집을 M개 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.
"""

# 2020/11/10 11:10 A.M. ~ 12:10 P. M.
# 실패 - 조합을 이용하여 문제를 풀면 간단하다.

n, m = map(int, input().split())

city = []
for _ in range(n):
    info = list(map(int, input().split()))
    city.append(info)

house = []
chicken = []
for r in range(n):
    for c in range(n):
        if city[r][c] == 1:
            house.append((r, c))
        elif city[r][c] == 2:
            chicken.append((r, c))

"""
chicken_distance = []
for h in house:
    for c in chicken:
        distance = abs(c[0]-h[0]) + abs(c[1]-h[1])
"""

from itertools import combinations # 조합을 사용하기 위해 외장 함수 호출

candidates = list(combinations(chicken, m)) # 조합을 이용하여 리스트 중 m개를 선택하여 후보군 생성

# 후보군의 치킨 거리의 합을 계산
def get_distance(candidate):
    result = 0
    # 모든 집에 대하여 검사
    for h in house:
        # 후보군 중 가장 가까운 치킨 집 찾기
        temp = 1e9
        for c in candidate:
            temp = min(temp, abs(h[0]-c[0])+abs(h[1]-c[1]))
        # 치킨 거리 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result

# 도시의 치킨 거리 찾기
result = 1e9
for candidate in candidates:
    result = min(result, get_distance(candidate))

print(result)