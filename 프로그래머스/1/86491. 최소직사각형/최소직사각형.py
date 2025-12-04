def solution(sizes):
    answer = 0
    sor = [sorted(i, reverse=True) for i in sizes]
    mam = max(i[0] for i in sor)           # 리스트안에 리스트의 첫번째 값들 중 최대값
    mam2 = max(i[1] for i in sor)
    answer = mam * mam2
    return answer