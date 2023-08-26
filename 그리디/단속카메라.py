def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    # print(routes)
    curr = -30000
    
    cam_cnt = 0
    
    for route in routes:
        if curr < route[0]:
            cam_cnt += 1
            curr = route[1]
    
    return cam_cnt



'''
채점 결과
정확성: 50.0
효율성: 50.0
합계: 100.0 / 100.0
'''
