
from itertools import combinations             # 순서무관, 중복제거 조합
def solution(numbers):
    answer = []
    answer = [sum(num2) for num2 in combinations(numbers, 2)]    # 조합으로 2개 고른 후 그 합의 리스트를 구함
    answer = sorted(set(answer))             # set은 중복값을 없애줌, sorted는 오름차순 정렬
    
    return answer