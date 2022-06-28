# 문자열 변환

# 정수 배열로 암호화 되어 있는 두 배열을 or 연산한 값에서 1: '#', 0: ' '으로 변환해서 출력
# 연산한 배열은 길이가 n인 정사각형 배열 형태


def solution_001(n, arr1, arr2):
    answer = []

    for i in range(n):
        # answer.append(format(arr1[i] | arr2[i], 'b').zfill(n))
        # answer.append('{0:b}'.format(arr1[i] | arr2[i]).zfill(n))
        answer.append('{0:b}'.format(arr1[i] | arr2[i]).rjust(n, '0'))

    def trans_result(text):
        trans_table = text.maketrans({'1': '#', '0': ' '})

        return text.translate(trans_table)

    print([trans_result(val) for val in answer])


def solution_002(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        calc = str(bin(i | j)[2:]).rjust(n, '0')
        calc = calc.replace('1', '#')
        calc = calc.replace('0', ' ')
        answer.append(calc)

    print(answer)


def solution_003(n, arr1, arr2):

    def line(n, x):
        # print(f'{x:016b}')
        return ''.join(' #'[int(i)] for i in f'{x:016b}'[-n:])

    print([line(n, a | b) for a, b in zip(arr1, arr2)])


# run result
n_001 = 6
arr1_001 = [46, 33, 33, 22, 31, 50]
arr2_001 = [27, 56, 19, 14, 14, 10]
solution_001(n_001, arr1_001, arr2_001)
solution_002(n_001, arr1_001, arr2_001)
solution_003(n_001, arr1_001, arr2_001)