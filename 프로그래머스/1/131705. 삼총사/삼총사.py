from itertools import combinations    # itertools.combinations : 리스트내의 값들의 조합을 구할때 사용(순서무관, 중복없음)

def solution(number):
    answer = 0
    comb = []
    comb = list(combinations(number, 3))       # number리스트에 있는 모든 값중 3개를 고르는 조합구하기
    for i in comb :
        if sum(i) == 0 :
            answer += 1

    return answer
# itertools.permutations : 순서중요, 중복없음
# itertools.product : 순서중요, 중복허용 (데카르트의 곱)