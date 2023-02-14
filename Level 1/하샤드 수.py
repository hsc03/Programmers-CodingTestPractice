'''
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 
자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, ,solution을 완성해주세요
'''

def solution(x):
    answer = True
    x_list = list(map(int, str(x)))
    hap = 0
    for i in x_list:
        hap += i
        if x % hap == 0:
            answer = True
        else:
            answer = False
    print(answer)
    return answer

solution(10)
solution(12)
solution(11)
solution(13)