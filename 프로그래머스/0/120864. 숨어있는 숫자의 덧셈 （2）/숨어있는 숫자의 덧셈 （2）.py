## 어렵어렵

def solution(my_string):
    answer = 0
    num = ''      # 숫자를 누적할 임시 문자열

    for ch in my_string:
        if ch.isdigit():       ## 숫자인지 판별-isidgit()
            num += ch          # 숫자면 계속 붙이기
        else:
            if num:             ## num이 빈문자열이 아니라면이라는 뜻(지금까지 누적된 숫자가 있는가)
                answer += int(num)  # num에 있는 숫자문자열을 정수로 변환
                num = ''        # 다음으로 num을 초기화하여 다음 숫자문자열을 누적할 준비함

    if num:                     # 마지막 숫자 처리, num이 빈문자열이 아니라면
        answer += int(num)
# 숫자 끝을 알리는 기준이 문자였기 때문에 문자열 끝에 숫자가 있으면 기존 조건에서 합산되지 않음, 따라서 마지막 숫자는 반복문이 끝난 후 따로 처리해야 함 그래서 마지막 숫자는 따로 if절 쓰는거임
    return answer