
import csv
import os
try:
    import pymysql
except ImportError:
    os.system('pip install pymysql')
    import pymysql
try:
    from matplotlib import pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure 
except ImportError:
    os.system('pip install matplotlib')
    from matplotlib import pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
import tkinter as tk
from tkinter import Toplevel, ttk
mycon = pymysql.connect(host = "localhost",user = "root",passwd = "1605")
mycur = mycon.cursor()
mycur.execute('create database if not exists expense_tracker;')
mycur.execute('use expense_tracker;')
root =tk.Tk()
root.geometry('300x250')
root.title('Expense Tracker')

def totalamount():
    top = Toplevel(root)
    top.title('Total amount')
    label= tk.Label(top, text='Total amount')
    label.grid(row=0, column=0)
    labelbox = tk.Entry(top, textvariable=tk.StringVar())
    labelbox.grid(row=0, column=1)
    def quitagain():
        top.destroy()
    def submit():
        with open('Check.txt','w') as f:
            labelval = labelbox.get()
            f.write(labelval)
    submi = tk.Button(top, text='Submit', command=submit)
    submi.grid(row=1, column=0)
    button = tk.Button(top, text='Quit',command=quitagain)
    button.grid(row=1, column=1)
mycur.execute('create table if not exists tracker(Date char(10), Expense char(25), Category char(25), Amount int(10), Balance int(10));')
mycur.execute('select * from tracker;')
fetch = mycur.fetchall()
tot_amount = 0
if fetch == ():
    with open('Check.txt', 'r') as f:
        tot_amount = int(f.read())
        temp = tot_amount
else:
    tot_amount = fetch[-1][-1]
    with open('Check.txt', 'r') as f:
        temp = int(f.read())
print(tot_amount)
print(temp)
def quit():
    root.destroy()
def create():
    global tot_amount
    top =Toplevel(root)
    top.geometry('200x200')
    top.title('Enter details')
    date = tk.Label(top, text='Date(YYYY-MM-DD)')
    date.grid(row=0, column=0)
    datebox = tk.Entry(top, textvariable=tk.StringVar())
    datebox.grid(row=0, column=1)
    expense = tk.Label(top, text="Expense")
    expense.grid(row=1, column=0)
    expensebox = tk.Entry(top, textvariable=tk.StringVar())
    expensebox.grid(row=1, column=1)
    category = tk.Label(top, text='Category of expense')
    category.grid(row=2, column=0)
    categorybox = tk.Entry(top, textvariable=tk.StringVar())
    categorybox.grid(row=2, column=1)
    amount = tk.Label(top, text='Amount')
    amount.grid(row=3, column=0)
    amountbox = tk.Entry(top, textvariable=tk.IntVar())
    amountbox.grid(row=3, column=1)
    def buton_func():
        global tot_amount
        datevalue = datebox.get()
        expensevalue = expensebox.get()
        categoryvalue = categorybox.get()
        amountvalue = amountbox.get()
        tot_amount = tot_amount - int(amountvalue)
        st = "insert into tracker values('{}','{}','{}',{},{})".format(datevalue, expensevalue, categoryvalue, amountvalue, tot_amount)
        mycur.execute(st)
        mycon.commit()
    def quit2():
        top.destroy()
    button = tk.Button(top, text='Submit',command=buton_func)
    button.grid(row=4, column=0)
    button_d = tk.Button(top, text='Quit', command=quit2)
    button_d.grid(row=4, column=1)
def display():
    global tot_amount
    top = Toplevel(root)
    top.geometry('1000x400')
    top.title('Display details')
    mycur.execute('select * from tracker;')
    fetch = mycur.fetchall()
    label1 = tk.Label(top, text='Total amount: '+str(temp))
    label1.grid(row=0, column=0) 
    frn = tk.Frame(top)
    frn.grid(row=3, column=0)
    tv = ttk.Treeview(frn, columns = (1,2,3,4,5), show='headings')
    tv.pack()
    tv.heading(1, text='Date')
    tv.heading(2, text='Expense')
    tv.heading(3, text='Category')
    tv.heading(4, text='Amount')
    tv.heading(5, text='Balance')
    for i in fetch:
        tv.insert('','end', values=i)
    label2 = tk.Label(top, text='Total balance: '+str(fetch[-1][-1]))
    label2.grid(row=1, column=0)
    def quit3():
        top.destroy()
    button_l = tk.Button(top, text='Quit', command=quit3)
    button_l.grid(row=4, column=0)
def report1():
    top = Toplevel(root)
    top.title('Enter date')
    date1 = tk.Label(top, text='Date(YYYY-MM-DD)')
    date1.grid(row=0, column=0)
    datebox = tk.Entry(top, textvariable=tk.StringVar())
    datebox.grid(row=0, column=1)
    def table():
        newtop = Toplevel(top)
        newtop.title("That day's expense")
        datevar = datebox.get()
        mycur.execute('select * from tracker where date="{}"'.format(datevar))
        fetch1 = mycur.fetchall()
        frn = tk.Frame(newtop)
        frn.grid(row=0, column=0)
        tv = ttk.Treeview(frn, columns = (1,2,3,4,5), show='headings')
        tv.pack()
        tv.heading(1, text='Date')
        tv.heading(2, text='Expense')
        tv.heading(3, text='Category')
        tv.heading(4, text='Amount')
        tv.heading(5, text='Balance')
        for i in fetch1:
            tv.insert('','end', values=i)
    datebutton = tk.Button(top, text='Submit', command=table)
    datebutton.grid(row=1, column=0)
    def quit4():
        top.destroy()
    button_q = tk.Button(top, text='Quit', command=quit4)
    button_q.grid(row=1, column=1)
def pie_chart():
    top = Toplevel(root)
    top.title('Enter month')
    month = tk.Label(top, text='Enter the month to get a overview of your expenses: ')
    month.grid(row=0, column=0)
    monthbox = tk.Entry(top, textvariable=tk.IntVar())
    monthbox.grid(row=0, column=1)
    def write():
        newtop = Toplevel(top)
        newtop.title('Pie Chart')
        mycur.execute('select * from tracker where Date like "_____{}%";'.format(monthbox.get()))
        fetch = mycur.fetchall()
        with open('expense.csv','w',newline='') as f:
            writer = csv.writer(f)
            for i in fetch:
                rec = [i[0],i[2]]
                writer.writerow(rec)
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
            graphtab = tk.Frame(newtop)
            graphtab.pack()
            fig = Figure()
            ax = fig.add_subplot(111)
            ax.pie(nper, radius=1, labels=nl,autopct='%0.2f%%', shadow=True,)
            canvas = FigureCanvasTkAgg(fig, graphtab)
            canvas.get_tk_widget().pack()
            canvas.draw()
    def quit5():
        top.destroy()
    button_k = tk.Button(top, text='Quit', command=quit5)
    button_a = tk.Button(top,text='Submit', command=write)
    button_a.grid(row=1, column=0)
    button_k.grid(row=1, column=1)
with open('Check.txt', 'r') as f:
    x = f.readlines()
    if x == []:
        button = tk.Button(root, text='Enter total amount', command=totalamount)
        button.grid(row=0, column=0)
        button1 = tk.Button(root, text='Enter deatils', command=create)
        button1.grid(row=1, column=0)
        button2 = tk.Button(root, text='Display', command=display)
        button2.grid(row=2, column=0)
        button3 = tk.Button(root, text='Expense of that day', command=report1)
        button3.grid(row=3, column=0)
        button4 = tk.Button(root, text='Expense of that month in a pie chart', command=pie_chart)
        button4.grid(row=4, column=0)
        button5 = tk.Button(root, text='Quit', command=quit)
        button5.grid(row=5, column=0)
    else:
        button1 = tk.Button(root, text='Enter deatils', command=create)
        button1.grid(row=0, column=0)
        button2 = tk.Button(root, text='Display', command=display)
        button2.grid(row=1, column=0)
        button3 = tk.Button(root, text='Expense of that day', command=report1)
        button3.grid(row=2, column=0)
        button4 = tk.Button(root, text='Expense of that month in a pie chart', command=pie_chart)
        button4.grid(row=3, column=0)
        button5 = tk.Button(root, text='Quit', command=quit)
        button5.grid(row=4, column=0)
label1 = tk.Label(root, text='Financial tips:')
label1.grid(row=6, column=0)
label2 = tk.Label(root, text='1.Create A Budget \n2.Use Cash Instead Of Plastic Money \n3.Create An Emergency Fund \n4.Set Financial Goals \n5.Avoid Taking On Debt')
label2.grid(row=7, column=0)
root.mainloop()
