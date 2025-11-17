def solution(spell, dic):
    answer = 2              # 기본값은 2 : 존재하지 않는 경우 
    str_spell = "".join(spell)    ## 리스트의 있는 문자를 문자열로 만들어줌
    for i in range(0, len(dic)) : 
        if sorted(str_spell) == sorted(dic[i]) :     # 정렬 후 비교(비교하는 경우 있으면 정렬하고 비교하는 방법 생각)
            answer = 1
            break          ## 찾았으면 바로 종료해줘야 함, 반복문이기 때문에 답이 계속 덮어씌여지기 때문에 끝내줘야함
        
    
    return answer