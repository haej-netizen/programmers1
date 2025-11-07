def solution(n):
    answer = []                          # answer라는 빈 리스트
    for i in range(1,n+1) :             # 약수이기 때문에 1~n+1 사이의 숫자만 가능
        if (n % i == 0) :
            answer.append(i)            #answer.append 자체 만으로 리스트에 추가됨

    return answer