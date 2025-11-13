def solution(my_string):
    answer = 0
    num = ''
    sign = 1
    for i in my_string :
        if i.isdigit() :
            num += i
        elif i == '+' :
            if num :
                answer += sign * int(num)
                num = ''
            sign = 1
        elif i == '-' :
            if num :
                answer += sign *int(num)
                num = ''
            sign = -1
    if num :
        answer += sign * int(num)
              
    return answer