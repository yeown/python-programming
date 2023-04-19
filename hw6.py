def display_multiplication_table(n):
    i=1
    while i <=9:
        for k in  range(n,n+4):
            print(f'{k} x {i} = {k * i:2d} \t', end = '')
        print()
        i += 1


display_multiplication_table(2)
print()
display_multiplication_table(6)
