import csv
import os
from re import T
try:
    import pymysql
except ImportError:
    os.system('pip install PyMySQL')
    import pymysql
try:
    from prettytable import PrettyTable
except ImportError:
    os.system('pip install prettytable')
    from prettytable import PrettyTable
try:
    from matplotlib import pyplot as plt
except ImportError:
    os.system('pip install matplotlib')
    from matplotlib import pyplot as plt
mycon = pymysql.connect(host = "localhost",user = "root",passwd = "akhilesh2005")
mycur = mycon.cursor()
mycur.execute('create database if not exists expense_tracker;')
mycur.execute('use expense_tracker;')
l=[]
tot_amount = 100000
temp =tot_amount
def create():
    global tot_amount
    mycur.execute('create table if not exists tracker(Date date, Expense char(25), Category char(25), Amount int(10), Balance int(10));')
    while True:
        date = input('Enter date in YYYY-MM-DD format: ')
        expense = input("Enter Expense: ")
        category = input('Enter category of expense: ')
        amount = int(input('Enter amount: '))
        tot_amount = tot_amount - amount
        st = "insert into tracker values('{}','{}','{}',{},{})".format(date, expense, category, amount, tot_amount)
        mycur.execute(st)
        mycon.commit()
        ch = input('Enter "y" to continue: ')
        if ch!= 'y':
            break
def display():
    global tot_amount
    l = ['Wants \n.Dining out \n.Entertainment \n.Travel','Financial Goals \n.Saving \n.Payind down loans', 'Needs \n.Rent/Mortgage \n.Utilities \n.Groceries \n.Transportation \n.Insurance Premiums']
    mycur.execute('select * from tracker;')
    fetch = mycur.fetchall()
    print('Total amount: ',temp) 
    x = PrettyTable()
    x.field_names = ["Date", "Expense", "Category", "Amount", "Balance"]
    for i in fetch:
        x.add_row([i[0],i[1],i[2],i[3],i[4]])
    print('Total balance: ',fetch[-1][-1])
    print('Tip: Keep total housing costs (rent/mortage + utilities) under 25-30% of your income')
    print(x)
def write():
    month = int(input('Enter the month to get a overview of your expenses: '))
    mycur.execute('select * from tracker where Date like "_____{}%";'.format(month))
    fetch = mycur.fetchall()
    with open('expense.csv','w',newline='') as f:
        writer = csv.writer(f)
        for i in fetch:
            rec = [i[0],i[2]]
            writer.writerow(rec)
def report1():
    date1 = input('Enter date in "YYYY-MM-DD" format: ')
    mycur.execute('select * from tracker where date="{}"'.format(date1))
    fetch1 = mycur.fetchall()
    y = PrettyTable()
    y.field_names = ['Date', 'Expense', 'Category', 'Amount', 'Balance']
    for i in fetch1:
        y.add_row([i[0],i[1],i[2],i[3],i[4]])
    print(y)
def pie_chart():
    l = []
    with open('expense.csv','r',newline='') as f:
        d = {}
        reader = csv.reader(f)
        for i in reader:
            l.append(i[1])
        for i in l:
            d[i]=(l.count(i)/len(l))*100
        nl = []
        nper = []
        for i in d:
            nl.append(i)
            nper.append(d[i])
        fig = plt.figure(figsize=(7,7))
        plt.pie(nper, labels=nl, autopct='%.1f%%')
        plt.show()
while True:
    print('1. Enter details')
    print('2. Display the records')
    print("3. Display that day's total expense report ")
    print("4. Display that month's total expense through pictorial representation")
    print("5. Exit")
    ch = int(input('Enter choice: '))
    if ch == 1:
        create()
    if ch == 2:
        display()
    if ch == 3:
        report1()
    if ch == 4:
        write()
        pie_chart()
    if ch == 5:
        break
    else:
        print('Invalid choice')
