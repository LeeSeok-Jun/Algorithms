"""
국영수
- https://www.acmicpc.net/problem/10825
- N명의 이름과 국어, 영어, 수학 점수가 주어질 때 다음과 같은 조건으로 학생의 성적을 정렬
    (1) 국어 점수가 감소하는 순으로
    (2) 국어 점수가 같으면 영어 점수가 증가하는 순서로
    (3) 국어 점수와 영어점수가 같으면 수학 점수가 감소하는 순서로
    (4) 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (대문자가 소문자 보다 먼저)

입력 조건
- 첫째 줄에 N명의 학생 수 주어진다.
- 둘째 줄 부터 한 줄에 하나 씩 각 학생의 이름, 국어, 영어, 수학 점수가 공백으로 주어진다.
- 점수는 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.
- 이름은 알파벳 대소문자로 이루어진 문자열이고 길이는 10자리를 넘지 않는다.

출력 조건
- 문제의 정렬 기준에 따라 N개의 줄에 걸쳐서 각 학생의 이름을 출력한다.
"""

# 풀이 제한 시간 : 20분
# 2020/12/02 11:33 ~ 11:51
# 실패 - 컴파일 시간 초과!

n = int(input())

data = []
for i in range(n):
    name, kor, eng, math = input().split()
    data.append((name, int(kor), int(eng), int(math)))

for i in range(len(data)):
    max_index = i

    for j in range(i + 1, len(data)):
        if data[max_index][1] < data[j][1]:
            max_index = j
        
        elif data[max_index][1] == data[j][1]:
            if data[max_index][2] > data[j][2]:
                max_index = j
            
            elif data[max_index][2] == data[j][2]:
                if data[max_index][3] < data[j][3]:
                    max_index = j

                elif data[max_index][3] == data[j][3]:
                    if data[max_index][0] > data[j][0]:
                        max_index = j

    data[i], data[max_index] = data[max_index], data[i]

for d in data:
    print(d[0])