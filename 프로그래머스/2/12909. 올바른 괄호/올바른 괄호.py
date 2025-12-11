def solution(s):
    stack = []
    
    for ch in s:
        if ch == '(':
            stack.append(ch)      # '('를 추가함
        else:   # ch == ')'
            ### stack에 요소가 있고(True) & 만약 직전이 '('라면 "()" → 즉시 제거
            if stack and stack[-1] == '(':
                stack.pop()   # 가장 마지막 요소 제거 및 반환
            else:
                return False
    
    return len(stack) == 0

# stack : 빈 리스트이면 False, 요소가 있으면 True로 평가됩니다.