from heapq import *

def solution(jobs): 
    answer, now, i = 0, 0, 0
    start = -10
    hq = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업들 저장
        for job in jobs:
            if start < job[0] <= now:
                heappush(hq, (job[1], job[0]))
    #-----------------------------------------#
        if hq:
            curr = heappop(hq)
            start = now
            now += curr[0]
            answer += now - curr[1]
            i += 1
            # print(curr, start, now, answer, i)
        else:
            now += 1
            # print(curr, start, now, answer, i)
    return answer // i
