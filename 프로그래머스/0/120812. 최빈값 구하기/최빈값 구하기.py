def solution(array):
    answer = 0
    max_count = 0
    multiple = False  # 최빈값이 여러 개인지 확인

    for num in array:  # 배열의 각 숫자 확인
        count = array.count(num)  # num이 몇 번 나왔는지 세기

        if count > max_count:  # 더 많이 나온 숫자가 있으면
            max_count = count
            answer = num
            multiple = False  # 새로운 최빈값 등장
        elif count == max_count and num != answer:  # 같은 최빈값가 여러 개
            multiple = True

    if multiple:
        return -1
    else:
        return answer