def solution(t, p):
    answer = 0
    num=0
    for i in range(len(t)-len(p)+1) : # 전체 문자열에서 p와 같은 길이의 숫자를 비교하고자 함
        num = int(t[i:i+len(p)])      # 비교할 숫자는 전체 문자열 중 [시작하는지점 : 시작지점+len(p)]
        if int(p) >= num :
            answer += 1
        
    return answer