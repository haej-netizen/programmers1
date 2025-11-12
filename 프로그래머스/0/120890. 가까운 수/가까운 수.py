##어렵어렵

def solution(array, n):
      
    min_diff = abs(array[0] - n)        
# <배열에서 최소값찾을때> 배열의 첫번째 값을 최소값으로 변수 지정 먼저 해놓고 배열의 두번째 값부터 시작하는 반복문을 통해서 최소값이랑 배열의 값을 계속 비교함, 그 후 최소값 변수에 진짜 최소값을 대입하는 방법 
    answer = array[0]
    for i in array[1:] :                ## 절댓값구할 때 abs는 숫자에만 씌울 수 있음
        diff = abs(n-i)                 # 배열의 수와 n의 차이를 절댓값으로 만들어서 비교함
        if diff < min_diff or (diff == min_diff and i < answer):  
###이 (~~) 조건은 동점 처리용입니다, “가장 가까운 값” 자체는 없어도 되지만,문제 요구사항에 “동일 차이면 더 작은 수 선택”이 있다면 필수
            min_diff = diff
            answer = i
    
    return answer


