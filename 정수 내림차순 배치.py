'''
함수 solution은 정수 n을 매개변수로 입력받습니다. 
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
'''

def solution(n):
    num = list(map(int, str(n)))
    num.sort()
    num.reverse()
    num2 = ''.join(map(str, num))
    answer = int(num2)
    print(answer)
    return answer

solution(118372)