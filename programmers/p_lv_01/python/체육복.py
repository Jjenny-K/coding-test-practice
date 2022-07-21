# 탐욕법 # 경우의 수

# 전체 학생 수 n, 체육복을 도난당한 학생 번호 배열 lost, 여벌의 체육복이 있는 학생 번호 배열 reserve
# 여벌의 체육복은 바로 앞번호나 뒷번호의 학생에게만 빌려줄 수 있음
# 체육수업을 들을 수 있는 최대 학생 수 출력


def solution_001(n, lost, reserve):
    answer = 0
    students = [i for i in range(1, n + 1)]
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for v in set_lost:
        if v - 1 in set_reserve:
            answer += 1
            set_reserve.remove(v - 1)
        elif v + 1 in set_reserve:
            answer += 1
            set_reserve.remove(v + 1)

    for v in students:
        if v not in set_lost:
            answer += 1

    return answer


def solution_002(n, lost, reserve):
    _reserve = sorted(r for r in reserve if r not in lost)
    _lost = sorted(l for l in lost if l not in reserve)
    
    for r in _reserve:
        f = r - 1
        b = r + 1

        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)

    return n - len(_lost)


n_001 = 8  # answer = 8
lost_001 = [1, 2, 3, 4]
reserve_001 = [1, 2, 3, 4]
print(solution_001(n_001, lost_001, reserve_001))
print(solution_002(n_001, lost_001, reserve_001))