def solution(genres, plays):
    answer = []
    genres_plays = zip(genres, plays)
    
    dict0 = {} # 장르, 횟수 정보를 저장하는 딕셔너리
    dict1 = {} # 장르별 총 저장 횟수를 저잫아는 딕셔너리
    for idx, elem in enumerate(genres_plays):
        # print(idx, elem)
        genre, play = elem[0], elem[1]

        if genre in dict0:
            dict0[genre].append((idx, play))
        else:
            dict0[genre] = [(idx, play)]
        
        dict0[genre].sort(reverse=True)
        dict1[genre] = dict1.get(genre, 0) + play # @#@#$@#$@#
        
    # print(dict0)
    # print(dict1)
    
    # 2500 600 800 500
    #    4   1   3   0
    # 총 재생횟수가 많은 걸 처음 항목으로 삼는다.
    
    # 총 횟수 표기 딕셔너리 재생횟수 기준으로 내림차순 정렬
    for genre, total_play in sorted(dict1.items(), key=lambda x: x[1], reverse=True):
        # print(genre, total_play)
        for idx, play in sorted(dict0[genre], key=lambda x: (-x[1],x[0]))[:2]:
            # print(dict0[genre])
            # print(idx, play)
            answer.append(idx)
    
    return answer
   
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# key=lambda x: (-x[1],x[0]) 
# - 첫 번째 항목을 기준으로 내림차순 정렬 후, 같은 값 있을 때 두번째 조건으로 오름차순 정렬하여 한번 더 필터링



'''
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
