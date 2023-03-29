def get_fixed_price(cut,name):
    price=int(input(name+ ' 상품의 할인된 가격은?'))
    result=price/(100-cut)*100
    return result
    



rate=int(input('할인율은?'))
Aprice=get_fixed_price(rate,'A')
Bprice=get_fixed_price(rate, 'B')
print('A 상품의 정가는', int(Aprice), '원')
print('B 상품의 정가는', int(Bprice), '원')
