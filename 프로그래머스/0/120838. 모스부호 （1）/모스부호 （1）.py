def solution(letter):
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    
    alp = list(morse.values())    # 모스부호가 딕셔너리 형태임, 키와 밸류 각각을 리스트로 변환
    mor = list(morse.keys())      # 키를 리스트로 변환
    lett =list(letter.split(' ')) # 주어진 모스부호letter를 공백으로 쪼개서 리스트로 변환
    
    for i in letter.split(' ') :  # 문자열.split()-- 이것만으로 리스트로 만들어짐
        for j in mor :
            if i == j :
                answer += alp[mor.index(i)] ###  이게 핵심이었던것, 문자를 차곡차곡 쌓아야함
               

    
    
    return answer