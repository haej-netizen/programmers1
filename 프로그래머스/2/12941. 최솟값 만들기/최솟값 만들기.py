def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=True)
    answer += A[-1]*B[-1]
    for i in range(len(A)-1) :
        answer += A[i]*B[i]
    

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer