def exchange(amount):

    n500=amount//500
    amount %=500

    n100=amount//100
    amount %=100

    n50=amount//50
    amount %=50

    n10=amount//10
    amount %=10


    print('>500원',n500, '개')
    print('>100원',n100, '개')
    print('>50원',n50, '개')
    print('>10원',n10, '개')
    
def get_integer(prompt):
    res=int(input(prompt))
    return res
    
change=get_integer('동전으로 교환하고자 하는 금액은?')
exchange(change)


