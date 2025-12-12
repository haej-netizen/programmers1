def solution(s):
    answer = ''
    string = []
    string = s.split(" ")
    
    answer = [i[0].upper() + i[1:].lower() if i else i for i in string]     # if i else i : 공백이 있는 경우 고려
    answer = " ".join(answer)
    return answer