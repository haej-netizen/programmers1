def solution(i, j, k):
    answer = 0
    for num in range(i,j+1) :
        
        string_num = str(num)
        for s in string_num :             # num에서 숫자와 k를 비교하기 위함
            
            if s == str(k) :    ## 'k'가 아닌 str(k)
                answer += 1        # 개수 세기
        
    return answer