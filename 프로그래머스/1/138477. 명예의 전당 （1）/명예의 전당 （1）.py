def solution(k, score):
    answer = []
    sco = []
# 점수를 일단 새로운 리스트에 넣으면서 몇등까지만 구하고 그중에 최소값을 answer리스트에 계속추가함, score에 있는 개수만큼 반복 
    for i in range(len(score)) :
        sco.append(score[i])
        sco = sorted(sco, reverse=True)[:k]    #오름차순정렬 후 k번째까지만 반환(명예의 전당에 있는 점수만 반환)
        answer.append(min(sco))
        
    return answer