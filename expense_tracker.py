
import csv
import os

try:
    from prettytable import PrettyTable
except ImportError:
    os.system('pip install prettytable')
    from prettytable import PrettyTable
tot_amount = float(input('Total amount: '))
def tracker():
    global tot_amount
    f = open('expense.csv','a',newline='')
    writer = csv.writer(f)
    writer.writerow(['Total amount: ' + str(tot_amount)])
    tracker = ["{:<10} {:<75} {:<10} {:<10}".format('Date','Expenses','Amount','Balance')]
    writer.writerow(tracker)
    date = input('Enter date: ')
    while True:
        expense = input('Enter expense: ')
        amount = float(input('Enter amount: '))
        balance = tot_amount - amount
        writer.writerow(["{:<10} {:<75} {:<10} {:<10}".format(date,expense,amount,balance)])
        ch = input('continue? Y/N').lower()
        if ch != 'y':
            break
def display():
    global tot_amount
    f = open('expense.csv','r',newline='')
    reader = csv.reader(f)
    print('Total amount: ',tot_amount)
    for i in reader:
        x = PrettyTable(["Date", "Expense", "Amount", "Balance"])
        x.add_row([i[0],i[1],i[2],i[3]])
        print(x)
def report1():
    global tot_amount
    f = open('expense.csv','r',newline='')
    reader = csv.reader(f)
    date = input("Enter date: ")
    next
    totsum = 0
    for i in reader:
        if i[0] == date:
            totsum += i[2]
            balance = tot_amount - totsum
    print('Total expense: ',totsum)
    print('Total balance: ',balance)
tracker()
display()
report1()
