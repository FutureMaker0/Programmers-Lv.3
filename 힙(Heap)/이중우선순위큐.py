from heapq import *

def solution(operations):
    heap = []
    
    for operation in operations:
        # print(operation.split(' ')[0], operation.split(' ')[1])
        command = operation.split(' ')[0]
        num = int(operation.split(' ')[1])
        
        if command == 'I':
            heappush(heap, num)
            # print(heap)
            
        elif command == 'D' and num == -1:
            if not heap:
                continue
            else:
                heappop(heap)
            # print(heap)
        
        elif command == 'D' and num == 1:
            if not heap:
                continue
            else:
                heap.remove(max(heap))
            # print(heap)
            
    # print(heap)
    if heap:
        return [int(max(heap)), int(min(heap))]
    return [0, 0]
    
