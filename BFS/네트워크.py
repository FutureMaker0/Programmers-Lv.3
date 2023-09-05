from collections import deque

def solution(n, computers):
    answer = 0
    dq = deque()
    
    visited = [False] * n
    
    for i in range(n):
        print(f'i = {i}')
        
        if not visited[i]:
            dq.append(i)
            visited[i] = True
            print(dq, visited)
            
            while dq:
                node = dq.popleft()
                print(f'dq = {dq}')
                print(f'node = {node}')
                
                for j in range(n):
                    print(f'j = {j}')
                    
                    if computers[node][j] == 1 and not visited[j]:
                        dq.append(j)
                        visited[j] = True
                        print(dq, visited)
                        
            answer += 1
            print(answer)
    
    return answer
