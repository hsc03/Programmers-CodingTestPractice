'''
정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 
단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
'''

def solution(arr):
    answer = []
    new_arr = sorted(arr, reverse=True)
    min_num = new_arr.pop(-1)
    arr.remove(min_num)

    if len(arr) != 0:
        for i in arr:
            answer.append(i)
    else:
        answer.append(-1)
    print(answer)
    return answer

solution([4, 3, 2, 1])
solution([10])