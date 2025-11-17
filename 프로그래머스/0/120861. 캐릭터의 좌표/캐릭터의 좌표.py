def solution(keyinput, board):
    answer = [0, 0]  # 초기 좌표 [x, y]
    max_x = board[0] // 2
    max_y = board[1] // 2

    # 각 키 입력 순서대로 처리
    for key in keyinput:
        if key == "up":
            if answer[1] < max_y:
                answer[1] += 1
        elif key == "down":
            if answer[1] > -max_y:
                answer[1] -= 1
        elif key == "right":
            if answer[0] < max_x:
                answer[0] += 1
        elif key == "left":
            if answer[0] > -max_x:
                answer[0] -= 1

    return answer
