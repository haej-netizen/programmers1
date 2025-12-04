
def solution(s):
    answer = []
    string = {}  ## 딕셔너리로 하는 이유-문자와 위치를 짝지어 저장하기 위해서

    for idx, ch in enumerate(s):       ## enumerate : 문자열에서 “위치(인덱스) + 문자”를 동시에 가져옴
        if ch not in string:
            answer.append(-1)
        else:
            answer.append(idx - string[ch])
        string[ch] = idx   ## 현재 인덱스로 최신화

    return answer