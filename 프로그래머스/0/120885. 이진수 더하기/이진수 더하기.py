def solution(a, b):
    a = a.zfill(max(len(a), len(b)))  ## ㅁ.zfill()-문자열 앞에 0을 채워서 자릿수를 맞춤
    b = b.zfill(max(len(a), len(b)))
    carry = 0       # 올림수 설정
    result = ''
    
    for i in range(len(a)-1, -1, -1):       # (시작, 끝, 순서)--(오른쪽)1의 자리부터 계산해야함
        total = carry
        total += int(a[i]) + int(b[i])
        result = str(total % 2) + result  # total % 2 → 현재 자리 결과 (0 또는 1)을 결과에 오른쪽부터 더해줌
        carry = total // 2                 # 1 + 1 이상 이면 올림수 추가 
        
    if carry:
        result = '1' + result           # 올림수가 남아있다면 1을 앞쪽에 추가해줌
    return result