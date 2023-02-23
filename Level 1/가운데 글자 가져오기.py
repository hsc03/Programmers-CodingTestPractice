'''
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 
단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
'''

def solution(s):
    answer = ''
    count = 0
    dict = {}
    
    for i in s:
        count += 1
        dict[count] = i
        
    str1 = dict.get(count // 2 + 1)
    str2 = dict.get(count // 2)
    
    if count % 2 == 0:
        answer = str2+str1
    else:
        answer = str1
    return answer