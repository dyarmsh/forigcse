def shop_stock():
    #task 1
    prodid = []
    stockno = []
    prices = []
    for i in range(0,3):
        prod_id = input('ENTER PRODUCT ID:')
        prodid.append(prod_id)
        stock = int(input('ENTER STOCK NUMBER:'))
        stockno.append(stock)
        price = int(input('ENTER PRICE:'))
        prices.append(price)

    print(prodid)
    print(stockno)
    print(prices)

    #task 2
    prod = input('INPUT THE PRODUCT ID:')
    for i in range(0,3):
        if prod == prodid[i]:
            stockno[i] = stockno[i] - 1
            print('NET STOCK:', stockno[i])       
            print('TOTAL BILL: $', prices[i])
            
    #task 3
    for i in range(0,3):
        if stockno[i] < 50:
            print(prodid[i], ': THIS PRODUCT NEEDS TO BE REODERED!')
       
shop_stock()
