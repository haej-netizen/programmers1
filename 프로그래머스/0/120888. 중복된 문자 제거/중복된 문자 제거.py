def solution(my_string):
    answer = ''
    for i in my_string :
        if i not in answer :  # if ~ not in --- 없으면 문자열에 더해주기
            answer += i
                
                
    return answer

# 문자열에서 중복 제거할 때 새 문자열에 하나씩 확인하면서 추가하는 것이 안전 
# 그냥 문자열이므로 리스트 변환 안함




