from itertools import combinations

def solution(dots):
    answer = 0
    for (x1,y1),(x2,y2) in combinations(dots, 2):        # 두 점 추출
        for (x3,y3),(x4,y4) in combinations(dots, 2):    # 또 다른 두 점 추출
            if len({(x1,y1),(x2,y2),(x3,y3),(x4,y4)}) == 4:   ## 이부분은 서로 다른 4개의 선분임을 확인하기 위함
                if (y2-y1)*(x4-x3) == (y4-y3)*(x2-x1) :      # 나누기로 풀면 실수로 나와서 곱하기로 푸는 것 권장
                    answer = 1
    
    return answer