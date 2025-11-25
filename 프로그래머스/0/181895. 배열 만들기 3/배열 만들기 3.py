def solution(arr, intervals):
    answer = []
    
    a1 = intervals[0][0]
    b1 = intervals[0][1]
    a2 = intervals[1][0]
    b2 = intervals[1][1]
    
    answer.append(arr[a1:b1+1])
    answer.append(arr[a2:b2+1])
    answer = sum(answer,[])     # 리스트안에 리스트를 푸는 방법
    return answer