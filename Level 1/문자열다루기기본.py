'''
문자열 s의 길이가 4 혹은 6이고, 
숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
'''

def solution(s):
    answer = True
    
    try:
        if len(s) == 4 or len(s) == 6: #문자열 s의 길이가 4 혹은 6인지 확인
            for i in s:
                int(i)  #문자열을 정수형으로 변환
        else:
            answer = False
            
    except ValueError:  #해당 에러 발생 시 answer을 False로 전환
        answer = False
        
    return answer