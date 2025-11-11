def solution(before, after):
    answer = 0
    sort_bef = sorted(before)   # 문자열의 구성요소가 동일한지 판단할 때 <<정렬>>한 후 비교하면 됨
    sort_aft = sorted(after)     
    
    if sort_bef == sort_aft :
        answer = 1
    else :
        answer = 0
    
    return answer