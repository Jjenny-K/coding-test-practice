# 자료 구조 # list

# 배열 seoul 원소 중 'Kim'의 위치를 찾아 임의 형태로 출력


def solution(seoul):
    # return '김서방은 {}에 있다'.format(seoul.index('Kim'))
    return '김서방은 %d에 있다' %seoul.index('Kim')


# run result
seoul_001 = ["Jane", "Kim"]  # answer = '김서방은 1에 있다'
print(solution(seoul_001))