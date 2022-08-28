import csv
no = 1
l = []
sep = []
gt1 = None


def bill():
    global gt1
    global no
    global l
    while True:
        today = input('Enter date: ')
        sno = 1
        invoice = ''
        if no == 0:
            invoice += str(today) + '-' + '001'
        if no > 0 and no < 10:
            invoice += str(today) + '-' + '00' + str(no)
        elif no > 10 and no < 100:
            invoice += str(today) + '-' + '0' + str(no)
        elif no > 100:
            invoice += str(today) + '-' + str(no)
        with open('Invoice.csv', 'a', newline='') as f:
            sr = csv.writer(f)
            s = [
                ['                          AK STORE                      '],
                ['                    A.G.s Colony, Nanganallur          '],
                ['                         chennai-66'],
                ['Date:' + str(today), '                                      Invoice no.:' + invoice]
                ]
            sr.writerows(s)
            sr.writerow(['S.No', 'Product', 'Quantity', 'Price', 'Total'])
        with open('Invoice.csv', 'a', newline='') as f:
            gt = 0
            r = csv.writer(f)
            while True:
                product = input('Enter Product name: ')
                quantity = int(input("Enter quantity: "))
                price = int(input('Enter product price: '))
                total = quantity * price
                gt += total
                bill = [sno, product, quantity, price, total]
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
                 ['GST: 2%'],
                 ['Grand total:' + ' ' + str(gt1) + '  ' + 'rupees'],
                 ['Discount: 10%' if discount() else ''],
                 ['Total amount Payable:' + ' ' + str(gt1) + ' ' + 'rupees only']]
            r.writerows(s)
            r.writerow([])
        l.append([today, invoice, product, quantity, gt1])
        ch1 = input('Next customer? (Y/N)').lower()
        if ch1 == 'y':
            no += 1
        elif ch1 == 'n':
            break


def between(l):
    sum = 0
    date = ''
    inv = ''
    pro = ''
    for i in l:
        date += i[0] + ' '
        inv += i[1] + ' '
        pro += i[2] + ' '
        sum += i[4]
    print('Dates: ', date)
    print('Invoice no: ', inv)
    print('Products: ', pro)
    print('Total amount sold: ', sum)


bill()
between(l)

