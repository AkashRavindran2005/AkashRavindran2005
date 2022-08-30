import csv

no = 1
l = []
gt1 = None
t = []


def bill():
    global t
    global gt1
    global no
    global l
    while True:
        today = input('Enter date: ')
        sno = 1
        invoice = ''
        if no < 10:
            invoice += str(today) + '-' + '00' + str(no)
        elif 10 <= no < 100:
            invoice += str(today) + '-' + '0' + str(no)
        elif no >= 100:
            invoice += str(today) + '-' + str(no)
        with open('Invoice.csv', 'a', newline='') as f:
            sr = csv.writer(f, delimiter = ' ')
            s = [
                ['                          Annachi Kadai                      '],
                ['                    A.G.s Colony, Nanganallur          '],
                ['                         chennai-66'],
                ['GSTin: 33EPJPS3261D1ZX ', '                                    Phone no: 9384802999'],
                ['Date:' + str(today), '                                      Invoice no.:' + invoice]
                ]
            sr.writerows(s)
            st = ["{:<5} {:<17} {:<15} {:<5} {:<8} {:<8}".format('S.no', 'Id', 'Description', 'QTY', 'MRP', 'Amount')]
            sr.writerow(st)
            with open('products.csv', 'r', newline='') as f1:
                reader = csv.reader(f1)
                print('{:<100} {:<5}'.format('Products', 'Stocks'))
                n=[]
                try:
                    for i in reader:
                        n.append(i)
                        print('{:<100} {:<5}'.format(i[0], i[1]))
                except:
                    print('')
                gt = 0
                r = csv.writer(f, delimiter = ' ')
                while True:
                    product = input('Enter Product name: ')
                    quantity = int(input("Enter quantity: "))
                    found = 0
                    try:
                        for rec in n:
                            if product.lower() in rec[0].lower():
                                rec[1] = str(int(rec[1]) - quantity)
                                found = 1
                            t.append(rec)
                    except:
                        print('')
                    if found == 0:
                        print('not found')
                    else:
                        with open('products.csv','w',newline='') as f2:
                            writer = csv.writer(f2)
                            writer.writerows(t)
                    price = int(input('Enter product price: '))
                    ind = id(product)
                    total = quantity * price
                    gt += total
                    pro = [product, ind, quantity]
                    l.append(pro)
                    bill = ["{:<5} {:<17} {:<15} {:<5} {:<8} {:<8}".format(sno, ind, product, quantity, price, total)]
                    sno += 1
                    r.writerow(bill)
                    ch = input('Next Product? (Y/N)').lower()
                    if ch == 'n':
                        break
                gt1 = (2/100)*gt + gt

            def discount():
                global gt1
                if gt1 > 5000:
                    gt1 = gt1 - (10 / 100) * gt1
                    return True
            s = [['Total:' + ' ' + str(gt) + '  ' + 'rupees'],
                 ['GST%: 2%'],
                 ['GST: ' + str((2/100)*gt) + 'rupees'],
                 ['Grand total:' + ' ' + str(gt1) + '  ' + 'rupees'],
                 ['Discount: 10%' if discount() else print('')],
                 ['Total amount Payable:' + ' ' + str(gt1) + ' ' + 'rupees only']]
            sr.writerows(s)
            sr.writerows([[],[]])
        l.append([today, invoice, gt1, ''])
        ch1 = input('Next customer? (Y/N)').lower()
        if ch1 == 'y':
            no += 1
        elif ch1 == 'n':
            break


def between(l,t):
    sum = 0
    date = ''
    invi = ''
    pro = ''
    id = ''
    stocks = ''
    for i in l:
        if len(i) == 3:
            for j in t:
                if i[0].lower() in j[0].lower():
                    stocks += j[1] + ',' + ' '
            pro += i[0] + ',' + ' '
            id += str(i[1]) + ',' + ' '
        else:
            date += i[0] + ',' + ' '
            invi += str(i[1]) + ',' + ' '
            sum += i[2]

    print('Dates: ', date)
    print('Invoice no: ', invi)
    print('Product id: ', id)
    print('Products: ', pro)
    print('Total amount sold: ', sum)
    print("Stocks left: ",stocks)


def order(t):
    f = []
    for i in t:
        if i[1].isdigit():
            if int(i[1]) <= 10:
                print('Placed order for',i[0])
                i[1] = str(100)
        f.append(i)
    with open('products.csv','w',newline='') as f1:
        writer = csv.writer(f1)
        writer.writerows(f)


def read():
    with open('Invoice.csv','r',newline='') as f:
        sr=csv.reader(f)
        for i in sr:
            for j in i:
                print(j)



bill()
between(l,t)
order(t)
read()
