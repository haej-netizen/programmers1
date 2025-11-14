def solution(balls, share):
    answer = 0 
    n_fact = 1              # 변수 초기 설정 필수!!
    m_fact = 1
    nm_fact = 1
    for i in range(1,balls+1) :
        n_fact *= i                 # 팩토리얼 구하는 방법
    for j in range (1, share+1) :
        m_fact *= j
    for k in range(1, balls-share+1) :
        nm_fact *= k
        
    answer = n_fact / (m_fact * nm_fact)
    return answer