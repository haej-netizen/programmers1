def solution(num_list, n):
    # 리스트를 일정 개수(n개)로 묶어서 리스트로 만들기
    answer = [num_list[i:i+n] for i in range(0, len(num_list), n)]
    
    #인덱스 i부터 i+n 직전까지의 요소를 잘라서 새 리스트로 반환
    #0부터 시작해서 len(data)까지 (즉, 데이터의 길이만큼) n씩 증가
    
    return answer