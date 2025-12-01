def solution(n, m):
    original_n, original_m = n, m  # 원래 값 저장

    # 유클리드 호제법으로 GCD 계산
    while m:
        n, m = m, n % m         # 최대공약수 구할때
    gcd = n

    # LCM 계산(최소공배수)
    lcm = (original_n * original_m) // gcd

    return [gcd, lcm]