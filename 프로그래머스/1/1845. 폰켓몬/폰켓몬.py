def solution(nums):
    unique = list(set(nums))      # 중복제거-set
    n = len(nums)//2
    answer = min(len(unique), n)     # 다른 숫자들의 개수와 뽑는 숫자의 개수(n) 중 작은값이 정답
    return answer