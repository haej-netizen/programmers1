import numpy as np

def solution(n, arr1, arr2):
    # 파이썬 리스트 → NumPy 배열 변환
    a1 = np.array(arr1)
    a2 = np.array(arr2)

    # 비트 OR 연산 (NumPy는 벡터 연산 자동 적용됨)-----np.bitwise_or:행렬 OR 연산 가능
    merged = np.bitwise_or(a1, a2)

    answer = []
    for num in merged:
        # 이진수 + n자리수 고정
        binary = format(num, f'0{n}b')

        # 비트맵 변환: 1 → '#', 0 → ' '
        row = binary.replace('1', '#').replace('0', ' ')
        answer.append(row)

    return answer