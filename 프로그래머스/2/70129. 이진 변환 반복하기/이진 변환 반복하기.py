def solution(s):
    answer = []
    zero = 0
    count = 0
    while s != "1" :
        
        zero += s.count("0")         # 0의 개수 세기
        s = s.replace("0","")        # 0을 찾아서 제거해줌
              
        s = bin(len(s))[2:]        # 0을 제거한 후 길이를 이진법으로 표현함
        count += 1
        
  
    return [count, zero]