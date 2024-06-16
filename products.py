products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': #quit
		break
	price = input('請輸入商品價格: ')
	#p = []
	#p.append(name)
	#p.append(price)
	#products.append(p)
	products.append([name, price])
for i in products:
	print('商品', i[0], '的價格是', i[1])

with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')