def solution(num, k):
    answer = -1   # answer의 기본값을 -1로 해줘야 없을때 -1 반환
    num_str = str(num) # num을 문자열로 바꿔 줌
    
    for i in num_str:
        if i == str(k) :
            answer = (num_str.find(str(k)) + 1)
        
            
    return answer

#이게 더 효율적인 함수인듯..
#def solution(num, k):
#   if str(k) in num_str:
#        return num_str.find(str(k)) + 1  
#    else:
#       return -1