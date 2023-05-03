shopping_bag=[]

print('[구입]')
while True:
    item = input('상품명? ')
    if item =='':
        break
    shopping_bag. append(item)
    count = int(input('수량은?'))
    if item == '':
        break
    shopping_bag. append(count)
    
    print(f'장바구니에 {item} {count}개가 담겼습니다.\n')

print(f'\n>>> 장바구니 보기: {shopping_bag}')

print('[검색]')
while True:
    item = input("장바구니에서 확인하고자하는 상품은? ")
    if item in shopping_bag:
            print(f"{item}은(는) {count}개 담겨 있습니다.")
    if input("계속 쇼핑하시겠습니까? (y/n) ").lower() != "y":
        break
   


