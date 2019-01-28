home_id = []
house_price = []
house_area = []
highest = 0
sold = []
sold_no = 0

for i in range(0,3):
    homeid =(input('ENTER HOUSE ID:'))
    home_id.append(homeid)
    houseprice = int(input('ENTER HOUSE PRICE:'))
    house_price.append(houseprice)
    housearea = int(input('ENTER HOUSE AREA:'))
    house_area.append(housearea)

for i in range(0,3):
    if  house_price[i] > highest:
        highest = house_price[i]

print('DETAILS OF MOST EXPENSIVE HOUSE:')
print(highest, ':PRICE OF MOST EXPENSIVE HOUSE')
print(home_id[i], ':HOME ID OF MOST EXPENSIVE HOUSE')
print(house_area[i], ':AREA OF MOST EXPENSIVE HOUSE')

while input != 'quit':
    houseid = int(input('ENTER HOME ID OF HOUSE YOU WOULD LIKE TO SEARCH:'))
    if houseid == home_id[i]:
        sold.append(houseid)
        sold_no = sold + 1
        print('AREA:', house_area[i])
        print('PRICE:', house_price[i])
print(sold_no, 'NUMBER OF HOUSES SOLD')
        



    
