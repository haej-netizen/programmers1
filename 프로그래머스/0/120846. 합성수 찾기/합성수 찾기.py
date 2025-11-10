def solution(n):
    answer = 0
    
    for i in range(1,n+1) : # 1~n까지 수 중에서 합성수를 구함
        c = 0           # c는 약수의 개수
        for j in range(1,i+1) : 
            if i % j == 0 :    # 약수 개수 증가
                c += 1
        if c >= 3 :   # 약수가 세 개 이상이므로 합성수 개수에 포함
            answer += 1
                
    return answer