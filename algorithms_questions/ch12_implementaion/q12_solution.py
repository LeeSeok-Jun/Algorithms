"""
기둥과 보 설치 - 해설
"""

# 현재 설치된 구조물이 조건에 맞는지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        # 기둥 검사
        if stuff == 0:
            # 기둥이 바닥 위에 있거나 보의 한쪽 끝 부분 위인 경우 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False

        # 보 검사
        elif stuff == 1:
            # 한쪽 끝 부분이 기둥 위 혹은 양쪽 끝 부분이 다른 보와 동시에 연결인 경우 정상
            if [x, y-1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    
    return True

def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, operate = frame
        
        # 삭제
        if operate == 0:
            answer.remove([x,y,stuff]) # 먼저 삭제를 진행하고 검사
            if not possible(answer):
                answer.append([x,y,stuff]) # 삭제 불가능할 경우 복구
        if operate == 1:
            answer.append([x,y,stuff]) # 먼저 설치해보고
            if not possible(answer):
                answer.remove([x,y,stuff]) # 설치 불가능 할 경우 삭제

    return sorted(answer)