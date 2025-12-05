def solution(s, n):
    answer = ''                 ## 알파벳 문자열을 사용해서 문제 풀기
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    ## 인덱스함수를 이용해서 일정 숫자만큼 더해서 알파벳을 반환함
    for i in s :
        if i in alphabet :
            answer += alphabet[(alphabet.index(i)+n)%26]   ## z다음에 a가 다시 나올 수 있도록 26으로 나눈 나머지 사용
        elif i in alphabet_upper :
            answer += alphabet_upper[(alphabet_upper.index(i)+n)%26] 
        else :      # 공백이 있는 경우
            answer += i
    
    return answer