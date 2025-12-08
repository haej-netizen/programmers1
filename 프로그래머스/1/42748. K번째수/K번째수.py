def solution(array, commands):
    answer = []
    
    for i in range(len(commands)) :  #  for one, two, three in commands:---이렇게 줄일수 있음
        one = commands[i][0]
        two = commands[i][1]
        three = commands[i][2]
        
        sliced = array[one-1:two]
        sliced = sorted(sliced)
        answer.append(sliced[three-1])        ## 리스트에 추가하는 것으로 답변 반환
    return answer