def solution(quiz):
    answer = []
    
    ## equation = [x.split(" ") for x in quiz]---2차원 리스트로 만들어버림
    for i in quiz :                       ###--- 1차원 리스트로 만들어야함
        equation = i.split(" ")
        
        befo = int(equation[0])  
       
        afte = int(equation[2])
        result = int(equation[4])
        if '+' in equation :      
            if befo + afte == result :
                answer.append("O")
            else : 
                answer.append("X")

        if '-' in equation :
            if befo - afte == result :
                answer.append("O")
            else :
                answer.append("X")

    return answer

