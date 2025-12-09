def solution(cards1, cards2, goal):
    idx1, idx2 = 0, 0  # 카드 더미의 현재 위치(=맨 위 카드)

    ## card1부터 차례대로 +1 하면서 goal과 비교하고 cards2도 차례대로 비교하면서 없으면 no반환하는 방법
    for word in goal:  # goal을 앞에서부터 확인
        if idx1 < len(cards1) and cards1[idx1] == word:
            # idx1 < len(cards1) → 카드를 더 꺼낼 수 있는 상태인지 확인
            idx1 += 1  # cards1에서 사용했으니 다음 카드로 이동(차례대로 비교하므로 그냥 +=1 사용)
        elif idx2 < len(cards2) and cards2[idx2] == word:
            idx2 += 1  # cards2에서 사용했으니 다음 카드로 이동
        else:
            return "No"  # 둘 중 어디에도 없으면 만들 수 없음

    return "Yes"  # 끝까지 통과했다면 성공