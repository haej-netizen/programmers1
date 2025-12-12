def solution(n):
    answer = 0
    
    
    k = 1  # 연속된 수의 개수
    while k * (k - 1) // 2 < n:   # a가 양수일 가능성이 있을 때만 검사
        if (n - k * (k - 1) // 2) % k == 0:
            answer += 1
        k += 1
    
    return answer

# N=k⋅a+2k(k−1) ---연속된 수의 합을 구하는 공식(a:시작, k:개수)