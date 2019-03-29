#task 1:
itemno = []
descr = []
resprice = []
buyerno = []
bidno = []
bidprice = []
nobid = []
nobidprice = []
inp = 'y'
status = []
sold = 0
notsold = 0
totalfee = []
nobids = 0

#for sellers:
item = int(input('ENTER NO. OF ITEMS: '))
if item < 0:
    print('ERROR')
    print('**************************************************')
else:
    print('***************************************************')
    for i in range (0,item):
        item_no = input('ENTER ITEM NUMBER: ')
        itemno.append(item_no)
        descrip = input('ENTER DESCRIPTION: ')
        descr.append(descrip)
        resp = int(input('ENTER RESERVE PRICE: '))
        resprice.append(resp)
        bidno.append(0)
        nobid.append(0)
        bidprice.append(0)
        totalfee.append(0)
        status.append('NOT SOLD')
        print('**************************************************')

print("ITEM NO\t\t\tITEM DESCRIPTION\tRESERVE PRICE\t")
for i in range (0, item):
    print(itemno[i],"\t\t\t",descr[i],"\t\t\t",resprice[i])

#task 2:
#for buyers:
while inp == 'y':
    print('**************************************************')
    itemn = input('ENTER ITEM NUMBER YOU WANT TO BID: ')
    for i in range (0, item):
        track = 0
        if itemn == itemno[i]:
            print('****************************************')
            print('DETAILS: ')
            print("ITEM NO\t\t\tITEM DESCRIPTION\tRESERVE PRICE\tSTATUS")
            print(itemno[i],"\t\t\t",descr[i],"\t\t\t",resprice[i],'\t\t', status[i])
            print('****************************************')
            
            buyer_no = int(input('ENTER BUYER NUMBER: '))
            buyerno.append(buyer_no)
            bid_price = int(input('ENTER YOUR BID PRICE: '))
            
            if bid_price > resprice[i]:
                bidprice[i]=(bid_price)
                print('BID SUCCESSFUL!')
                status[i]=('SOLD')
                bidno[i] += 1
                print('CURRENT NUMBER OF BIDS: ', bidno[i], 'for item: ', itemno[i])

                
                
    
            else:
                nobidprice.append(bid_price)
                exit
                print('SORRY. YOUR BID IS LESSER THAN RESERVE PRICE.')
                nobid[i] += 1

            print('***************************************************')
            print(bidno[i], ' bids :NUMBER OF SUCCESSFUL BIDS FOR ITEM: ', itemno[i])
            print('**************************************************')

            
            inp = input('DO YOU WISH TO CONTINUE? (y/n): ')

print('**************************************************')
for d in range(0, item):
    print('ITEM: ', itemno[d], 'HAS ', bidno[d], 'BIDS.') 


#task 3:
for i in range (0, item):
    if bidprice[i] >= resprice[i]:
        status[i] = 'SOLD'
        sold += 1
        fee = int(bidprice[i])
        totalfee[i] = (fee * 1.1)
        print('TOTAL FEE:', totalfee[i], 'FOR ITEM:', itemno[i])

    else:
        status[i]=('NOT SOLD')
        print('ITEM: ', itemno[i], 'WAS NOT SOLD.')
        notsold += 1

    if bidno[i] == 0:
        print(itemno[i], ':HAS NO BIDS')
        nobids += 1

    elif nobid[i] == 1:
        print('ITEMS WHICH DID NOT REACH THEIR RESERVE PRICE:')
        print("ITEM NO\t\t\tFINALBID")
        print(itemno[i],'  ', nobidprice[i])
                
print('BIDS LESSER THAN RESERVE PRICE:', nobid[i])
print('NUMBER OF ITEMS SOLD/ NOT SOLD:', sold, '/', notsold)
print('NUMBER OF ITEMS WITH NO BIDS:', nobids)


    
   
