# 어렵어렵
from itertools import permutations    ## 순서를 고려하는 조합(permutation)
# from itertools import combinations--- combination은 순서를 무시하므로 답이 안나올 수 있음
def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    possible = set()                      ## set으로 하면 중복을 허용하지 않고 검색(in)이 매우 빠름(list말고 set이용)
    
    for i in range(1, 5):
        for c in permutations(words, i):      ## 조합들을 구하는 방법
            possible.add(''.join(c))          ## 조합들을 구하는 방법, set인 경우 add사용
    
    for b in babbling:
        if b in possible:
            answer += 1
            
    return answer