store = {}
for i in range(n):
    item = input()
    quantity = input()
    price = input()
    totalprice = quantity * price
    store[item] = store.get(item,0) + totalprice

    total = 0
    for key, val in store.items():
        if maxcost < val:
            maxcost = item
        avg = totalprice / (i+1)
print ("Item: {} \nTotal price: {:.2f} \n Average cost: {:.2f}".format(item, avg, maxcost))