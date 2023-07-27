# 각 원소의 곱이 최대이려면, 두 수의 표준편차가 최소여야 한다. 표준편차의 개념을 알아야 코드를 짠다.
# 이게 lv.3이다... difficult...

def solution(n, s):
    # n = 2, s = 9
    answer = []
    quotion, remainder = divmod(s, n)
    # quotion = 4, remainder = 1

    if not quotion:
        return [-1]
    
    for _ in range(n-remainder): # n-remainder는 몫과 같은 값 (2-1=1)
        answer.append(quotion) # 몫인 4가 들어간다
    
    for _ in range(remainder): # 나머지와 같은 횟수 1
        answer.append(quotion+1) 
    
    # answer = [quotion for _ in range(n - remainder)] + [quotion+1 for _ in range(remainder)]
    # 이 경우, 몫과 같은 (n-나머지)와 몫에 1을 더한 나머지 요소로 목록 응답을 초기화
    # 이렇게 하면 답에 있는 모든 요소의 합이 s와 같아지게 된다.
    # 이것이 합계가 s와 같은 n개의 양의 정수 목록을 나타낸다.
        
    return answer



'''
채점 결과
정확성: 70.0
효율성: 30.0
합계: 100.0 / 100.0
'''
