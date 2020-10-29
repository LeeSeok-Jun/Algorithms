# 입력 데이터가 많은 문제를 sys 라이브러리 readline() 함수를 이용
import sys

# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

# 입력받은 문자열 그대로 출력
print(input_data)