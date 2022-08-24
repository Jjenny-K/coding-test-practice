# 브루트 포스

# 종말의 숫자: 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수
# n번째 영화의 제목에 들어갈 종말의 숫자 출력

N = int(input())

title_number = 666
cnt = 1

while True:
    if N == 1:
        break

    title_number += 1

    if '666' in str(title_number):
        cnt += 1

    if N == cnt:
        break

print(title_number)