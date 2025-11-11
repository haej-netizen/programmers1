def solution(s):
    n_answer = ''
    
    for i in s :
        if s.count(i) == 1 :                 ## 문자열.count()-- 문자 개수 반환
            n_answer += i
            answer = "".join(sorted(n_answer))      ## sorted는 리스트를 반환하므로 문자열로 만들기 위해서 join 사용
    return answer