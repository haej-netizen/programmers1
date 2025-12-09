def solution(strings, n):
    answer = []
    answer = sorted(strings, key=lambda x: (x[n],x))   # n번째 숫자가 첫번째 정렬기준, 그냥 글자가 두번째 정렬기준
    return answer