# 완정 탐색 # 문자열 파싱

# 각 개인정보가 지정된 약관으로 수집되어지고, 약관마다 개인정보 보관 유효기간이 정해짐
# 오늘 날짜 today, 약관 유효기간 배열 terms, 수집된 개인정보 배열 privacies가 주어질 때, 오늘 날짜로 파기해야 할 개인정보 번호 출력
# terms는 '약관종류 유효기간' 형태의 문자열 배열, privacies는 '날짜 약관종류' 형태의 문자열 배열
# 한 달은 28일로 가정


def solution(today, terms, privacies):
    answer = []
    terms_dict = {}

    for term in terms:
        type, period = term.split()
        terms_dict[type] = int(period)

    year, month, day = map(int, today.split('.'))
    today_day = (year * 336) + (month * 28) + day

    for idx, privacy in enumerate(privacies, start=1):
        date, type = privacy.split()

        py, pm, pd = map(int, date.split('.'))
        date_day = (py * 336) + (pm * 28) + pd + (terms_dict[type] * 28)

        if today_day >= date_day:
            answer.append(idx)

    return answer


# run result
today_001 = '2020.01.01'  # answer = [1, 4, 5]
terms_001 = ["Z 3", "D 5"]
privacies_001 = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
print(solution(today_001, terms_001, privacies_001))