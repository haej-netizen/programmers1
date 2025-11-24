def solution(num, total):
    answer = []
    
    first = 0
    
    mul = (num) * (1+num)//2            # 1에 대한 등차수열의 합(등차수열의 합 공식 : n(2a+(n-1)d)/2
    first = (total-mul)//num          # 답의 첫번째 숫자 구하기
    
    for i in range(first+1, first+num+1): 
        answer.append(i)
    return answer