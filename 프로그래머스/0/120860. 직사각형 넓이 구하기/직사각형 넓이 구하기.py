def solution(dots):
    answer = 0
    sort_dots = sorted(dots, key=lambda x:x[0])
# 리스트내 리스트나 튜플 등이 있을 때 정렬하는 방법 : sorted(리스트명, key = lambda x:x[정렬기준]) 
    width = sort_dots[2][0] - sort_dots[1][0]
    height = sort_dots[1][1] - sort_dots[0][1]
    
    answer = width * height
    return answer