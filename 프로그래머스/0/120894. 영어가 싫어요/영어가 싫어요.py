def solution(numbers):
    answer = numbers  # 문자열로 시작-----비효율적인 방법
    
    if "zero" in answer:
        answer = answer.replace("zero", "0")
    if "one" in answer:
        answer = answer.replace("one", "1")
    if "two" in answer:
        answer = answer.replace("two", "2")
    if "three" in answer:
        answer = answer.replace("three", "3")
    if "four" in answer:
        answer = answer.replace("four", "4")
    if "five" in answer:
        answer = answer.replace("five", "5")
    if "six" in answer:
        answer = answer.replace("six", "6")
    if "seven" in answer:
        answer = answer.replace("seven", "7")
    if "eight" in answer:
        answer = answer.replace("eight", "8")
    if "nine" in answer:
        answer = answer.replace("nine", "9")
    
    return int(answer)

#효율적인 방법
#def solution(numbers):
#num_dict = {
 #       "zero":"0", "one":"1", "two":"2", "three":"3", "four":"4",
#        "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"
 #   }
    
 #   for word, digit in num_dict.items():  ---------##dict.items()은 딕셔너리에서 키,값을 쌍으로 갖고오는 함수
  #      numbers = numbers.replace(word, digit)  # 이전 결과에 계속 적용
  #  
  #  return int(numbers)
