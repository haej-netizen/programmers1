def solution(sides):
    answer = 0
    diff = abs(sides[0] - sides[1])       # 삼각형이 될 수 있는 조건 두값의 차이 < i < 두값의 합

    for i in range(0,sum(sides)) :
        if diff < i :
            answer += 1
            
    return answer