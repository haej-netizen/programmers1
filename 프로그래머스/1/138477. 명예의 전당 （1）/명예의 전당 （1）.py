def solution(k, score):
    answer = []
    sco = []
    for i in range(len(score)) :
        sco.append(score[i])
        sco = sorted(sco, reverse=True)[:k]
        answer.append(min(sco))
        
    return answer