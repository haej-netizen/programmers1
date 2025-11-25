## 어렵어렵
def solution(lines):
    # 선분을 편하게 변수로 풀기
    a_s, a_e = lines[0]
    b_s, b_e = lines[1]
    c_s, c_e = lines[2]

    # 두 선분의 겹침 길이
    def overlap(s1, e1, s2, e2):
        return max(0, min(e1, e2) - max(s1, s2))

    # 각 쌍의 겹침 합
    ab = overlap(a_s, a_e, b_s, b_e)
    ac = overlap(a_s, a_e, c_s, c_e)
    bc = overlap(b_s, b_e, c_s, c_e)

    # 세 선분이 모두 겹치는(공통) 구간 길이
    abc = max(0, min(a_e, b_e, c_e) - max(a_s, b_s, c_s))

    # 3겹 구간이 3번 세어진 것을 보정
    # (3겹 구간을 1번만 세야함)
    answer = ab + ac + bc - 2 * abc

    return answer