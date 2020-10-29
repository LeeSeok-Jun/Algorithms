"""
두 배열의 원소 교체
- N개의 자연수를 원소로 갖는 2개의 배열 A와 B가 존재한다.
- 배열 A와 B의 원소를 하나씩 골라 서로 바꾸는 최대의 K 번의 바꾸기 연산이 가능하다.
- 바꾸기 연산을 통해 배열 A의 모든 원소의 합이 최대가 되로록 한다.
- N, K 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합이 최댓값을 갖는 프로그램을 작성하시오.

입력 조건
- 첫 번째 줄에 N, K가 공백으로 구분되어 입력된다.(1 <= N <= 100,000, 0 <= K <= N)
- 두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.
- 세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다. 조건은 A와 같다.

출력 조건
- 최대 K번의 바꾸기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력한다.
"""

n, k = map(int, input().split()) # N과 K를 입력받기
a = list(map(int, input().split())) # 배열 A의 모든 원소 입력받기
b = list(map(int, input().split())) # 배열 B의 모든 원소 입력받기

a.sort() # 배열 A는 오름차순으로 정렬
b.sort(reverse=True) # 배열 B는 내림차순으로 정렬

# 첫 번째 인덱스부터 확인하여 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B보다 작은 경우 바꾸기 실행
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    # A의 원소가 B의 원소보다 크거나 같으면 반복문 탈출
    else:
        break

print(sum(a)) # 배열 A의 모든 원소의 합을 출력
