def solution(myString):
    answer = ''
   
    for i in myString :            
        if i < 'l' :
            answer += 'l'           # l보다 앞에일때 l로 바꿔주는 문자열을 새로 만드는 방법으로 해결
        else : 
            answer += i            # l보다 뒤에 일때 그냥 문자열에 포함시킴
            
    return answer
# replace 랑 for i~ 쓰면 i가 나오는 모든 것을 바꿔버리기 때문에 부적절