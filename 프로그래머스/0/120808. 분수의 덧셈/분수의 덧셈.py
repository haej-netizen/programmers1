def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    for i in range(max(denom1, denom2), denom1 * denom2 + 1):    # 최소공배수 구하는 반복문
        if i % denom1 == 0 and i % denom2 == 0:
            lcm = i                                              ## 반복문에서 최소를 구하려고 변수에 넣어줌     
            break                                                ## 반복문에서 최소를 구하려면 break해줘야함
    result1 = (lcm // denom1 * numer1) + (lcm //denom2 * numer2)   #분자 덧셈 계산
    
    for j in range(min(result1, lcm), 0, -1):     # 최대공약수 구하는 반복문(분자와 분모의 최대공약수를 구해야함)
        if result1 % j == 0 and lcm % j == 0:
            gcd = j
            break                                                  ## 반복문에서 최대를 구하려면 break해줘야함
    
    answer.append(result1 // gcd)                                # 최대공약수로 약분을 해줘야 정확한 값
    answer.append(lcm // gcd)
    
    return answer