def solution(id_pw, db):
    answer = ''
    
    for data in db :
        if data == id_pw :
            answer = 'login'
        elif data[0] == id_pw[0] :
            answer = 'wrong pw'
        elif data[1] != id_pw[1] :
            answer = 'fail'
            

        
    return answer