# 문자열 변환

# 신규 유저가 입력한 아이디 new_id가 주어질 때 아이디 규칙에 맞는 추천 아이디 출력
"""
    # 아이디 규칙
    1. new_id 모든 대문자를 소문자로 치환
    2. 알파벳 소문자, 숫자, '-', '_', '.'를 제외한 모든 문자 제거
    3. '.'가 2번 이상 연속될 경우 '.'(하나의 마침표)로 치환
    4. '.'가 처음이나 끝에 위치한다면 제거
    5. new_id가 비었을 경우 'a' 추가
    6. new_id 길이가 16자 이상일 경우 첫 15개 문자 제외한 모든 문자 제거(제거 후 '.'가 끝에 위치한다면 제거)
    7. new_id 길이가 2자 이하일 경우 new_id 길이가 3이 될 때까지 마지막 문자 반복 추가
"""
import re


def solution_001(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    new_id = re.sub(r'[.]{2,}', '.', new_id)
    new_id = new_id[1:] if new_id.startswith('.') else new_id
    new_id = 'a' if len(new_id) == 0 else new_id
    new_id = new_id[:15] if len(new_id) >= 16 else new_id
    # 상위에서 '.'(하나의 마침표)로 치환되기 때문에 일정 조건 이후 최종적으로 마지막 '.' 제거
    new_id = new_id[:-1] if new_id.endswith('.') else new_id
    new_id = new_id + ''.join(new_id[-1] for _ in range(3 - len(new_id))) if len(new_id) <= 2 else new_id

    return new_id


def solution_002(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    new_id = re.sub('\.+', '.', new_id)
    new_id = re.sub('^[.]|[.]$', '', new_id)
    new_id = 'a' if len(new_id) == 0 else new_id[:15]
    new_id = re.sub('^[.]|[.]$', '', new_id)
    new_id = new_id if len(new_id) > 2 else new_id + "".join([new_id[-1] for _ in range(3 - len(new_id))])

    return new_id


# run result
new_id_001 = '...!@BaT#*..y.abcdefghijklm'  # answer = 'bat.y.abcdefghi'
print(solution_001(new_id_001))
print(solution_002(new_id_001))