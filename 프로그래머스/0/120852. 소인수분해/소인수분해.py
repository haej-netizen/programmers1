def solution(n):
    answer = []
    divisor = 2                            # 가장 작은 소수 2부터 시작
    
    while n > 1 :                          ## while문으로 반복시키기
        if n % divisor == 0 :
            if divisor not in answer :      # 중복된 2를 지우기 위한 코드
                answer.append(divisor)
            n //= divisor                   ## (들여쓰기 주의), 몫을 다시 검사해서 소수를 구하는 과정
        else :
            divisor += 1                  # 나눠지지 않으면 다음 소수 판단하기
            
   
    return answer