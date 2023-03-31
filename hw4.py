name=input('Input his/her name:')

def rep_char(c, n):
    print(c*n)

def draw_line_string(name,msg2):
    msg1=f'Hello {name},'
    nstr=len(msg1) if(len(msg1)>len(msg2)) else len(msg2)
    rep_char('-', nstr +2)
    print(f' {msg1} \n {msg2}')
    rep_char('-', nstr +2)


draw_line_string(name,'Welcome to Seoul.')
