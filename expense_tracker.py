import csv
import os

try:
    from prettytable import PrettyTable
except ImportError:
    os.system('pip install prettytable')
    from prettytable import PrettyTable
with open('expense.csv','r',newline='') as f:
    reader = csv.reader(f)
    for i in reader:
        if i != []:
            pass
        else:
            tot_amount = float(input('Total amount: '))
def tracker():
    global tot_amount
    with open('expense.csv','a',newline='') as f: 
        with open('expense.csv','r',newline='') as file:
            writer = csv.writer(f,delimiter=' ')
            reader = csv.reader(file)
            for i in reader:
                if i != []:
                    pass
                else:
                    writer.writerow(['Total amount: ' + str(tot_amount)])
                    tracker = ["{:<10} {:<75} {:<10} {:<10}".format('Date','Expenses','Amount','Balance')]
                    writer.writerow(tracker)
            date = input('Enter date: ')
            while True:
                balance = 0
                expense = input('Enter expense: ')
                amount = float(input('Enter amount: '))
                for i in reader:
                    str = ''
                    if i[0] != []:
                        for j in i[0]:
                            for k in j:
                                if k.isdigit():
                                    str += k
                                if k == '.':
                                    break
                        balance += int(str) - amount
                    else:
                        balance += tot_amount - amount
                writer.writerow(["{:<10} {:<75} {:<10} {:<10}".format(date,expense,amount,balance)])
                ch = input('continue? Y/N').lower()
                if ch != 'y':
                    break
def display():
    global tot_amount
    with open('expense.csv','r',newline='') as f:
        reader = csv.reader(f)
        str = ''
        for i in reader:
            if i[0] != []:
                for j in i[0]:
                    for k in j:
                        if k.isdigit():
                            str += k
                        if k == '.':
                            break
                print('Total amount: ',str)
            else:
                print('Total amount: ',tot_amount)
        for i in reader:
            x = PrettyTable(["Date", "Expense", "Amount", "Balance"])
            x.add_row([i[0],i[1],i[2],i[3]])
            print(x)
def report1():
    global tot_amount
    with open('expense.csv','r',newline='') as f:
        reader = csv.reader(f)
        date = input("Enter date: ")
        next
        totsum = 0
        str = 0
        for i in reader:
            if i[0] == date:
                totsum += i[2]
                if i[0] != []:
                    for j in i:
                        for k in j:
                            str += k
                balance = k - totsum
            else:
                balance = tot_amount - totsum
        print('Total expense: ',totsum)
        print('Total balance: ',balance)
tracker()
display()
report1()
