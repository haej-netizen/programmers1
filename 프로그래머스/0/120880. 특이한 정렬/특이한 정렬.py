def solution(numlist, n):
    answer = []

    answer = sorted(numlist, key=lambda x: (abs(x-n), -x))
    # sorted(리스트명, key=lambda x: (정렬기준1, 정렬기준2))>>> (-x)라는 의미는 내림차순이라는 뜻
    # 차이의 절댓값 등 다양한 기준으로 정렬 가능
    return answer