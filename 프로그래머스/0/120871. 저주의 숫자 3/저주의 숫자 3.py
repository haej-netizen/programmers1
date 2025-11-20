def solution(n):
    numbers = []
    i = 1

    while len(numbers) < n:
        if i % 3 != 0 and '3' not in str(i): # 3의 배수이고 3이 들어가는 숫자가 아닐것
            numbers.append(i)
        i += 1
            
     
    answer = numbers[n-1]  # n번째 수 구하기
    return answer


# remove로 풀기에는 오류가 발생함
# if, elif 사용할때 중복이 발생하지 않도록 주의
