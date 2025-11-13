def solution(numbers, k):
    answer = 0
    numbers2 = numbers * k            # 리스트 numbers를 충분하게 반복
    
    numbers_even = numbers2[0::2]     # 리스트 numbers 반복한 리스트 중에서 짝수번째만 추출
    answer = numbers_even[k-1]        # 짝수번째만 추출한 리스트에서 k번째 숫자를 구함
    return answer