def solution(score):
    answer = []
    mean = []
    for i in score :
        mean.append(sum(i) / 2)    # 점수묶음의 평균을 평균리스트에 담음
    
    sort_mean = sorted(mean, reverse = True)       # 내림차순 정렬
    
    # 내림차순 정렬된 그 순서를 기존 순서대로 answer에 넣음
    for j in mean :        ## 여기서는 mean을 써야 기존 순서로 배치됨
        answer.append(sort_mean.index(j)+1)   # 여기서는 sort_mean을 써야 순서를 알려줌
    return answer

# 리스트.index() 사용 > 동점자 처리 불가
# for을 문장 안에 넣어서 사용 > 반복문을 한 줄에 담아 새로운 리스트를 빠르게 만들고 싶을 때(기존의 for문 + append를 한 줄로 표현하는 것), ex>>answer = [sort_mean.index(m) + 1 for m in mean]