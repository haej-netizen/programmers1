def solution(arr):
    answer = []
    answer.append(arr[0])      # arr의 첫번째값은 무조건 답에 포함
    for i in arr[1:] :         # arr의 두번째값부터 판단 
        if i != answer[-1] :   ## answer에 직전에 이미 추출된 값과 같은지로 연속 판단하는 것
            answer.append(i)
   
    return answer
# 연속되는 값이 있으면 하나만 추출하고 싶을때 <추출한> 답의 리스트에서 직전 값이 같은지로 연속 판단