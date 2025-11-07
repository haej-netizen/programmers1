def solution(my_string):
    answer = my_string.lower()
    arranged_answer= "".join(sorted(answer))
    return arranged_answer
