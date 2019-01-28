home_id = []
house_price = []
house_area = []
highestprice = 0
highestid = 0
highestarea = 0
sold = []
sold_no = 0

#task 1:
for i in range(0,3):
    homeid =(input('ENTER HOUSE ID:'))
    home_id.append(homeid)
    houseprice = int(input('ENTER HOUSE PRICE:'))
    house_price.append(houseprice)
    housearea = int(input('ENTER HOUSE AREA:'))
    house_area.append(housearea)

#task 2:
for i in range(0,3):
    if  house_price[i] > highest:
        highestprice = house_price[i]
        highestid = home_id[i]
        highestarea = house-area[i]
print('DETAILS OF MOST EXPENSIVE HOUSE:')
print(highestprice, ':PRICE OF MOST EXPENSIVE HOUSE')
print(highestid, ':HOME ID OF MOST EXPENSIVE HOUSE')
print(highestarea, ':AREA OF MOST EXPENSIVE HOUSE')

#task 3:
houseid = int(input('ENTER HOME ID OF HOUSE YOU WOULD LIKE TO BUY:'))
if houseid == home_id[i]:
    print('AREA:', house_area[i])
    print('PRICE:', house_price[i])
    inpt = input('WOULD YOU LIKE TO BUY THIS HOUSE?')
    if inpt == 'y':
        print('SOLD')
        sold.append(houseid)
        sold_no += 1
    elif inpt == 'n':
        print('NOT SOLD')

while input != 'quit':
    houseid = int(input('ENTER HOME ID OF HOUSE YOU WOULD LIKE TO BUY:'))
    if houseid == home_id[i]:
    print('AREA:', house_area[i])
    print('PRICE:', house_price[i])
    inpt = input('WOULD YOU LIKE TO BUY THIS HOUSE?')
    if inpt == 'y':
        if houseid != sold[i]:
            print('SOLD')
            sold.append(houseid)
        elif houseid == sold[i]:
            print('HOUSE IS ALREADY SOLD')
        sold_no += 1
    elif inpt == 'n':
        print('NOT SOLD')

#task 4:           
print(sold_no, 'NUMBER OF HOUSES SOLD')
