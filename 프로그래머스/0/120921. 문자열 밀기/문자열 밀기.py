def solution(A, B):
    answer = 0
    
    for i in range(len(A)) :    # 최대 A의 문자열 글자수 만큼 반복함
        if A == B :             ## 제일 먼저 A와 B가 같은지 판단
            return answer       # 같으면 끝
        A = A[-1] + A[:-1]      # 같지 않았기 때문에 (마지막 글자 + 나머지 앞글자)로 갱신
        answer += 1             # 횟수 더해주기, 다시 반복
        
    answer = -1                 # 글자수만큼 반복했는데 아직도 안같으면 -1
    return answer