def solution(numbers, direction):
  
     # answer = list(map(int, numbers.split(',')))----그냥 숫자 배열일 때 가져오기
    answer = numbers[:] #리스트 전체를 처음부터 끝까지 가져오기
    
    if direction == "right" :
                  
                  last = answer[len(answer)-1]  # 지우기 전에 last에 저장
                  del answer[len(answer)-1]      #del 리스트명[]     
                  answer.insert(0, last)         #리스트명.insert
                  
    else :
                  first = answer[0]        # 지우기 전에 first에 저장
                  del answer[0]
                  answer.append(first)     #리스트명.append
                  
    return answer