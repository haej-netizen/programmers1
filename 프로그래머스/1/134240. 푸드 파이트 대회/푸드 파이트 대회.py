def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer += str(i)*(food[i]//2)
    answer += '0'
    for j in range(len(food)-1,0,-1) :
        answer += str(j)*(food[j]//2)
    return answer