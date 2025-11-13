def solution(numbers, k):
    answer = 0
    numbers2 = numbers * k
    
    numbers_even = numbers2[0::2]
    answer = numbers_even[k-1]
    return answer