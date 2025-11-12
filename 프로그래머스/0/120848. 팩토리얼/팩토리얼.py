def solution(n):
    fact = 1
    i = 1

    while fact * i <= n:    # 1부터 계속 곱해지는 것
        fact *= i
        i += 1            # n보다 작을 때 계속 곱하면서 i는 1씩 증가

    return i-1             # i에 처음에 1이 들어갔으므로 빼줌