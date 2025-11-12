def solution(array):
    answer = 0
    for i in array:
        while i > 0:
            if i % 10 == 7:             # 자리 수를 판별하고 일의자리가 7인지 판별
                answer += 1
            i //= 10                    # 계속 반복하면 자리 수가 7인지 판별가능 (조건문 여러개 쓸 필요 없음)
    return answer

# def solution(array):          모범답안
#    count = 0
#    for num in array:
#       count += str(num).count('7')
#   return count