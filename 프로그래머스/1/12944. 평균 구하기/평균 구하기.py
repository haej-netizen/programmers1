def solution(arr):
    answer = 0
    sumsum = 0                # 합계 구하기
    for i in arr :
        sumsum += i           # arr에 있는 모든 합계 구하기
        answer = sumsum/len(arr)    # 평균구하기, 실수로 나올수도 있으므로 / 사용
    return answer