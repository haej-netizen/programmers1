def solution(age):
    
   # 숫자를 문자열로 변환
    age_str = str(age)

    # 각 숫자(문자)를 대응되는 알파벳으로 변환 (0→'a', 1→'b', ..., 9→'j')
    result = '' #--- 빈 통(문자열)을 먼저 준비해서 변환된 문자들을 차곡차곡 담는 과정
    
    for ch in age_str:
        result += chr(int(ch) + 97)   # 문자열을 합치는 과정

    return result
  



