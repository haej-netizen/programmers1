def solution(chicken) :
    answer = 0
    
    while chicken >= 10:                   # 치킨이 서비스를 받을 수 있는 경우에서는
        service = chicken // 10            # 서비스치킨 개수는 치킨 개수 나누기 10
        answer += service                  # 답은 서비스 개수이므로
        chicken = service + chicken % 10   # 서비스로 받은 치킨 + 10개가 안되는 쿠폰을 모아놓음

    return answer 


# 이렇게 풀면 0.1 제곱할 때 소수점이 컴퓨터에서 정확하게 표현되지 않아서 오류 발생하는 것     
#def solution(chicken):
#   import math
#   answer = 0
#        for i in range(1,1000000) :
#            answer += chicken*0.1**i 
#   return math.ceil(answer)
    
    
    