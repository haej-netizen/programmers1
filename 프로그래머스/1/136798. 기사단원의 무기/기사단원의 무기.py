def solution(number, limit, power):
    answer = 0
    # 약수 개수를 저장할 배열 (1~n)
    div = [0] * (number + 1)

        # i가 약수인 모든 수 j = i, 2i, 3i, ... 에 +1씩
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            div[j] += 1

    for d in div :
        if d > limit :
            answer += power
        else :
            answer += d
    return answer