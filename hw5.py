def read_single_digit(n):
    if n == '0':
        return '영'
    elif n== '1':
        return '일'
    elif n== '2':
        return '이'
    elif n=='3':
        return '삼'
    elif n== '4':
        return '사'
    elif n== '5':
        return '오'
    elif n== '6':
        return '육'
    elif n== '7':
        return '칠'
    elif n== '8':
        return '팔'
    elif n=='9':
        return '구'
    else:
        return ' '

def read_number(n):
    if len(n) == 1:
        return read_single_digit(n)
    elif len(n) == 2:
        a1 = read_single_digit(n[0])
        a2 = read_single_digit(n[1])
        return f'{a1} {a2}'
    elif len(n) ==3:
        a1 = read_single_digit(n[0])
        a2 = read_single_digit(n[1])
        a3 = read_single_digit(n[2])
        return f'{a1} {a2} {a3}'
    

n=input('세 자리 정수 입력:')
print(read_number(n))






