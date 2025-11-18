def solution(myString):
    answer = []
    split_str = myString.split('x')      # 문자열.split(기준문자)-- 기준문자를 기준으로 문자열을 나눔
    
    for i in range(len(split_str)) :
        answer.append(len(split_str[i]))      
# answer = answer.append(len(split_str[i]))---이렇게 하면 none밖에 안나옴, 그냥 answer.append(len(split_str[i]))으로만 작성
    return answer


## 더 간단한 버전
#  def solution(myString):
#      return [len(s) for s in myString.split('x')]