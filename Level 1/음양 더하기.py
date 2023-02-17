'''
어떤 정수들이 있습니다. 
이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 
실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
'''

def solution(absolutes, signs):
    count = 0
    result = []
    
    for i in signs:
        if i == True:
            result.append(absolutes[count])
        else:
            result.append(absolutes[count] * -1)
        count += 1
        
    answer = sum(result)
    print(answer)
    return answer

solution([4,7,12], [True,False,True])
solution([1, 2, 3], [False,False,True])