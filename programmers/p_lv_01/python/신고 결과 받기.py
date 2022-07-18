# 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송할 때 각 유저가 받은 처리 메일 수 출력
# 유저는 횟수에 제한 없이 한 번에 한 명의 유저를 신고 가능(동일한 유저에 대한 신고는 1회로 처리)
# k번 이상 신고된 유저는 게시판 이용이 정지되고 해당 유저를 신고한 유저에게 정지 사실을 메일로 발송
import collections


def solution_001(id_list, report, k):
    answer = []

    # 중복 신고 제거
    report = list(set(report))

    # 유저별 신고한 아이디 dict
    report_id = collections.defaultdict(list)
    # 유저별 신고당한 횟수 dict
    report_cnt = collections.defaultdict(int)

    for user in id_list:
        report_id[user]

    for v in report:
        x, y = v.split(' ')
        report_id[x].append(y)
        report_cnt[y] += 1

    # 정지된 아이디 list
    stop_id_list = [key for key, value in report_cnt.items() if value >= k]

    # 유저별 처리 결과 메일 받은 횟수 list
    for i in report_id:
        cnt = 0
        for j in report_id[i]:
            if j in stop_id_list:
                cnt += 1
        answer.append(cnt)

    print(answer)


def solution_002(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}

    # 유저별 신고받은 횟수 저장
    for r in set(report):
        reports[r.split()[1]] += 1

    # k번 이상 신고 받은 유저 처리 결과 발송 횟수 저장
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    print(answer)


# run result
id_list_001 = ["muzi", "frodo", "apeach", "neo"]
report_001 = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k_001 = 2
solution_001(id_list_001, report_001, k_001)
solution_002(id_list_001, report_001, k_001)