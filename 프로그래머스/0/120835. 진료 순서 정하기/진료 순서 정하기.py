def solution(emergency):
    answer = []
    sor_emer = sorted(emergency, reverse = True)   # emergency의 배열을 내림차순으로 정렬
    for i in emergency :
        
        num = sor_emer.index(i) +1  # 내림차순 배열에서 순서 찾기(리스트는 순서는 0부터 시작하므로 +1 해주기)
        answer.append(num)           # 순서를 리스트에 추가함
    return answer