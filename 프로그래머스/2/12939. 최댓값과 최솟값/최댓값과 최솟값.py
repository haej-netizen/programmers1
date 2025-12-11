def solution(s):
    answer = ''
    string = []
    string = s.split(" ")
    string = list(map(int, string))     
    ## map : 리스트의 모든 요소에 같은 함수를 적용하고, 변환된 값들을 묶어서 반환하는 도구
    string = sorted(string)
    answer += str(string[0])
    answer += ' '
    answer += str(string[-1])
    return answer