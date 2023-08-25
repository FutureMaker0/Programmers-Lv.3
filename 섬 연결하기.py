def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) # 비용기준으로 오름차순 정렬
    connect = set([costs[0][0]]) # 연결을 확인하는 집합
    print(costs, connect)

    while len(connect) != n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:
                continue
            elif cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                print(connect, answer)
                break # while문 검증을 위한 break
                # 일단 break 걸고 len 확인한다음 거짓이 될떄까지 for문 처음부터 다시 반복
    
    return answer
