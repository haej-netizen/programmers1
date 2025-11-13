def solution(s):
    answer = 0
    stack = []  # 숫자를 저장하는 스택
    for x in s.split():  # 공백을 기준으로 나눠서 리스트에 저장
        if x == 'Z':
            if stack:  # 스택에 숫자가 있으면 마지막 숫자 제거
                stack.pop()  #pop()함수 :마지막 요소를 꺼내서 반환하고, 동시에 그 요소를 삭제하는 함수
        else:
            stack.append(int(x))  # 숫자로 변환해서 추가
    answer = sum(stack)
    return answer
