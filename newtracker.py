import csv
import os
import mysql.connector as m
try:
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure 
except ImportError:
    os.system('pip install matplotlib')
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
try:
    import numpy
except ImportError:
    os.system('pip install numpy')
    import numpy
try:
    import customtkinter as tk
except ImportError:
    os.system('pip install customtkinter')
    import customtkinter as tk
import math
from tkinter import ttk, PhotoImage, messagebox
import datetime
from dateutil.relativedelta import relativedelta
import sv_ttk
mycon = m.connect(host = "localhost",user = "root",passwd = "1605")
mycur = mycon.cursor()
mycur.execute('create database if not exists expense_tracker;')
mycur.execute('use expense_tracker;')
root =tk.CTk()
root.geometry('825x325')
root.title('Expense Tracker')
image_icon=PhotoImage(file="budget.png")
root.iconphoto(False,image_icon)
tk.set_appearance_mode("dark")  
tk.set_default_color_theme("blue")
mycur.execute('create table if not exists tracker(Date char(10), Expense char(25), Category char(25), Amount int(10), Balance int(10));')
tot_amount = 0
temp = 0
def totalamount():
    global tot_amount
    global temp
    top = tk.CTkToplevel(root)
    top.title('Total amount')
    label= tk.CTkLabel(top, text='Total amount')
    label.grid(row=0, column=0)
    labelbox = tk.CTkEntry(master=top, textvariable=tk.StringVar())
    labelbox.grid(row=0, column=1)
    def quitagain():
        top.destroy()
    def submit():
        with open('Check.txt','w') as f:
            labelval = labelbox.get()
            f.write(labelval)
    submi = tk.CTkButton(master=top, text='Submit', command=submit, text_color="white",hover= True, hover_color= "#1a592b",border_width=2, border_color='#1a592b' ,corner_radius=20, bg_color="#262626",fg_color=None)
    submi.grid(row=1, column=0)
    button = tk.CTkButton(master=top, text='Quit',command=quitagain, text_color="white",hover= True, hover_color= "#1a592b",border_width=2, border_color='#1a592b' ,corner_radius=20, bg_color="#262626",fg_color=None)
    button.grid(row=1, column=1)
    mycur.execute('select * from tracker;')
    fetch = mycur.fetchall()
    tot_amount = 0
    if fetch == []:
        with open('Check.txt', 'r') as f:
            tot_amount = int(f.read())
            temp = tot_amount
    else:
        tot_amount = fetch[-1][-1]
        with open('Check.txt', 'r') as f:
            temp = f.read()
            temp = int(temp)
def quit():
    root.destroy()
def create():
    global tot_amount
    global temp
    mycur.execute('select * from tracker;')
    fetch = mycur.fetchall()
    tot_amount = 0
    if fetch == []:
        with open('Check.txt', 'r') as f:
            tot_amount = int(f.read())
            temp = tot_amount
    else:
        tot_amount = fetch[-1][-1]
        with open('Check.txt', 'r') as f:
            temp = f.read()
            temp = int(temp)
    top =tk.CTkToplevel(root)
    top.geometry('300x200')
    top.title('Enter details')
    date = tk.CTkLabel(master=top, text='Date(YYYY-MM-DD)')
    date.grid(row=0, column=0)
    datebox = tk.CTkEntry(master=top, textvariable=tk.StringVar())
    datebox.grid(row=0, column=1)
    expense = tk.CTkLabel(master=top, text="Expense")
    expense.grid(row=1, column=0)
    expensebox = tk.CTkEntry(master=top, textvariable=tk.StringVar())
    expensebox.grid(row=1, column=1)
    category = tk.CTkLabel(master=top, text='Category of expense')
    category.grid(row=2, column=0)
    categorybox = tk.CTkEntry(master=top, textvariable=tk.StringVar())
    categorybox.grid(row=2, column=1)
    amount = tk.CTkLabel(master=top, text='Amount')
    amount.grid(row=3, column=0)
    amountbox = tk.CTkEntry(master=top, textvariable=tk.IntVar())
    amountbox.grid(row=3, column=1)
    def buton_func():
        global tot_amount
        datevalue = datebox.get()
        expensevalue = expensebox.get()
        categoryvalue = categorybox.get()
        amountvalue = amountbox.get()
        tot_amount = tot_amount - int(amountvalue)
        st = "insert into tracker values('{}','{}','{}',{},{})".format(datevalue, expensevalue, categoryvalue, amountvalue, tot_amount)
        label = tk.CTkLabel(master=top, text='Record added successfully!')
        label.grid(row=4, column=0)
        mycur.execute(st)
        mycon.commit()
    def quit2():
        top.destroy()
    button = tk.CTkButton(master=top, text='Submit',command=buton_func, text_color="white",hover= True, hover_color= "#1a592b",border_width=2, border_color='#1a592b' ,corner_radius=20, bg_color="#262626",fg_color=None)
    button.grid(row=5, column=0)
    button_d = tk.CTkButton(master=top, text='Quit', command=quit2, text_color="white",hover= True, hover_color= "#1a592b",border_width=2, border_color='#1a592b' ,corner_radius=20, bg_color="#262626",fg_color=None)
    button_d.grid(row=5, column=1)
def display():
    global tot_amount
    global temp
    mycur.execute('select * from tracker;')
    fetch = mycur.fetchall()
    tot_amount = 0
    if fetch == []:
        with open('Check.txt', 'r') as f:
            tot_amount = int(f.read())
            temp = tot_amount
    else:
        tot_amount = fetch[-1][-1]
        with open('Check.txt', 'r') as f:
            temp = f.read()
            temp = int(temp)
    top = tk.CTkToplevel(root)
    top.geometry('800x400')
    top.title('Display details')
    mycur.execute('select * from tracker;')
    fetch = mycur.fetchall()
    label1 = tk.CTkLabel(master=top, text='Total amount: '+str(temp))
    label1.grid(row=0, column=0) 
    frn = tk.CTkFrame(master=top)
    frn.grid(row=3, column=0)
    style = ttk.Style()
    sv_ttk.set_theme('dark')
    tv = ttk.Treeview(frn, columns = (1,2,3,4,5), show='headings', selectmode='browse')
    tv.pack()
    tv.heading(1, text='Date')
    tv.heading(2, text='Expense')
    tv.heading(3, text='Category')
    tv.heading(4, text='Amount')
    tv.heading(5, text='Balance')
    for i in fetch:
        tv.insert('','end', values=i)
    label2 = tk.CTkLabel(master=top, text='Total balance: '+str(fetch[-1][-1]))
    label2.grid(row=1, column=0)
    def quit3():
        top.destroy()
    button_l = tk.CTkButton(master=top, text='Quit', command=quit3, text_color="white",hover= True, hover_color= "#1a592b",border_width=2, border_color='#1a592b' ,corner_radius=20, bg_color="#262626",fg_color=None)
    button_l.place(x=330, y=300)
def report1():
    top = tk.CTkToplevel(root)
    top.title('Enter date')
    date1 = tk.CTkLabel(master=top, text='Date(YYYY-MM-DD)', bg='#808080')
    date1.grid(row=0, column=0)
    datebox = tk.CTkEntry(master=top, textvariable=tk.StringVar(), bg='#808080')
    datebox.grid(row=0, column=1)
    def table():
        newtop = tk.CTkToplevel(top)
        newtop.title("That day's expense")
        datevar = datebox.get()
        mycur.execute('select * from tracker where date="{}"'.format(datevar))
        fetch1 = mycur.fetchall()
        frn = tk.CTkFrame(newtop)
        frn.grid(row=0, column=0)
        style = ttk.Style()
        sv_ttk.set_theme('dark')
        tv = ttk.Treeview(frn, columns = (1,2,3,4,5), show='headings')
        tv.pack()
        tv.heading(1, text='Date')
        tv.heading(2, text='Expense')
        tv.heading(3, text='Category')
        tv.heading(4, text='Amount')
        tv.heading(5, text='Balance')
        for i in fetch1:
            tv.insert('','end', values=i)
        def quit6():
            newtop.destroy()
        button_l = tk.CTkButton(master=newtop, text='Quit', command=quit6, text_color="white",hover= True, hover_color= "#1a592b",border_width=2, border_color='#1a592b' ,corner_radius=20, bg_color="#262626",fg_color=None)
        button_l.place(x=330, y=300)
    datebutton = tk.CTkButton(top, text='Submit', command=table, text_color="white",hover= True, hover_color= "#1a592b",border_width=2, border_color='#1a592b' ,corner_radius=20, bg_color="#262626",fg_color=None)
    datebutton.grid(row=1, column=0)
    def quit4():
        top.destroy()
    button_q = tk.CTkButton(top, text='Quit', command=quit4, text_color="white",hover= True, hover_color= "#1a592b",border_width=2, border_color='#1a592b' ,corner_radius=20, bg_color="#262626",fg_color=None)
    button_q.grid(row=1, column=1)
def pie_chart():
    top = tk.CTkToplevel(root)
    top.title('Enter month')
    month = tk.CTkLabel(master=top, text='Enter the month to get a overview of your expenses: ')
    month.grid(row=0, column=0)
    monthbox = tk.CTkEntry(master=top, textvariable=tk.IntVar())
    monthbox.grid(row=0, column=1)
    def write():
        newtop = tk.CTkToplevel(top)
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
            graphtab = tk.CTkFrame(master=newtop)
            graphtab.pack()
            fig = Figure(facecolor='#134567')
            ax = fig.add_subplot(111)
            ax.pie(nper, radius=1, labels=nl,autopct='%0.2f%%', shadow=True,)
            canvas = FigureCanvasTkAgg(fig, graphtab)
            canvas.get_tk_widget().pack()
            canvas.draw()
    def quit5():
        top.destroy()
    button_k = tk.CTkButton(master=top, text='Quit', command=quit5, text_color="white",hover= True, hover_color= "#1a592b",border_width=2, border_color='#1a592b' ,corner_radius=20, bg_color="#262626",fg_color=None)
    button_a = tk.CTkButton(master=top,text='Submit', command=write, text_color="white",hover= True, hover_color= "#1a592b",border_width=2, border_color='#1a592b' ,corner_radius=20, bg_color="#262626",fg_color=None)
    button_a.grid(row=1, column=0)
    button_k.grid(row=1, column=1)
def incomevsspending():
    top = tk.CTkToplevel(root)
    top.title('Income vs Expense graph')
    mycur.execute('select * from tracker;')
    with open('Income.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        fetch = mycur.fetchall()
        for i in fetch:
            l = [i[0]]
            writer.writerow(l)
    nl = {}
    with open('Income.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        for i in reader:
            for j in i:
                nl[j[5:7]] = None
    naml = []
    for i in nl:
        mycur.execute('select sum(Amount) from tracker where Date like "_____{}%";'.format(i))
        fetch = mycur.fetchall()
        for j in fetch:
            for k in j:
                naml.append(k)
    nlm = []
    with open('Check.txt', 'r') as f:
        x = f.read()
        nlm.append(x)
        nlm = nlm*len(naml)
    income = []
    for i in nlm:
        income.append(int(i))
    width = 0.4
    values = numpy.arange(len(naml))
    spend = [i+width for i in values]
    month = []
    for i in nl:
        month.append(int(i))
    frame = tk.CTkFrame(master=top)
    frame.pack()
    fig = Figure(figsize=(5,4), dpi=100, facecolor='#134567')
    a = fig.add_subplot(111)
    a.bar(values, income, width, label='Income')
    a.bar(spend, naml, width, label='Expense')
    a.set_xticks(values, month)
    a.set_xticks(range(3))
    a.set_xlabel('Month')
    a.set_ylabel('Amount')
    a.legend()
    canvas = FigureCanvasTkAgg(fig, frame)
    canvas.get_tk_widget().pack()
    canvas.draw()
def debt():
    new = tk.CTkToplevel(root)
    new.title('Loan calculator')
    new.geometry('250x150')
    def loanpayoff():
        payoff = tk.CTkToplevel(new)
        payoff.title('Loan free by')
        label0 = tk.CTkLabel(master=payoff, text='Date(YYYY-MM-DD)')
        label = tk.CTkLabel(master=payoff, text='Loan principal')
        label1 = tk.CTkLabel(master=payoff, text='Monthly payment')
        label2 = tk.CTkLabel(master=payoff, text='Loan Interest')
        entry0 = tk.CTkEntry(master=payoff, textvariable=tk.StringVar())
        entry = tk.CTkEntry(master=payoff, textvariable=tk.IntVar())
        entry1 = tk.CTkEntry(master=payoff, textvariable=tk.IntVar())
        entry2 = tk.CTkEntry(master=payoff, textvariable=tk.StringVar())
        label0.grid(row=0, column=0)
        label.grid(row=1, column=0)
        label1.grid(row=2, column=0)
        label2.grid(row=3, column=0)
        entry0.grid(row=0, column=1)
        entry.grid(row=1, column=1)
        entry1.grid(row=2, column=1)
        entry2.grid(row=3, column=1)
        def submit():
            d = entry0.get()
            cb = entry.get()
            mp = entry1.get()
            ir = entry2.get()
            i = float(ir)/(12*100)
            print(i)
            nm = math.log(float(mp)/(float(mp)-i*float(cb)),1+i)
            y = (math.ceil(nm))//12
            m = (math.ceil(nm))%12
            year = datetime.datetime(int(d[:4]), int(d[5:7]), int(d[-2:]))
            date = year + relativedelta(months = int(m))
            print(date)
            n = date + relativedelta(years=int(y))
            print(n)
            messagebox.showinfo('Debt free by', 'Debt free by '+ str(n.year) +'-'+ str(n.month)+'-'+str(n.day))
        def quit50():
            payoff.destroy()
        quit10 = tk.CTkButton(master=payoff, text='Quit', command=quit50, text_color="white",hover= True, hover_color= "#1a592b",border_width=2, border_color='#1a592b' ,corner_radius=20, bg_color="#262626",fg_color=None)
        quit10.grid(row=4, column=1)
        submi = tk.CTkButton(master=payoff, text='Submit', command=submit, text_color="white",hover= True, hover_color= "#1a592b",border_width=2, border_color='#1a592b' ,corner_radius=20, bg_color="#262626",fg_color=None)
        submi.grid(row=4, column=0)
    def monthlypayment():
        monthly = tk.CTkToplevel(new)
        monthly.title('Annuity monthly payment amount')
        label = tk.CTkLabel(master=monthly, text='Loan principal')
        label1 = tk.CTkLabel(master=monthly, text='No. of periods')
        label2 = tk.CTkLabel(master=monthly, text='Loan Interest')
        entry = tk.CTkEntry(master=monthly, textvariable=tk.IntVar())
        entry1 = tk.CTkEntry(master=monthly, textvariable=tk.IntVar())
        entry2 = tk.CTkEntry(master=monthly, textvariable=tk.StringVar())
        label.grid(row=0, column=0)
        label1.grid(row=1, column=0)
        label2.grid(row=2, column=0)
        entry.grid(row=0, column=1)
        entry1.grid(row=1, column=1)
        entry2.grid(row=2, column=1)
        def submit():
            cb = entry.get()
            np = entry1.get()
            ir = entry2.get()
            i = float(ir)/(12*100)
            annuity = float(cb)*((float(i)*(1+float(i))**float(np))/((1+float(i))**float(np)-1))
            mp = math.ceil(annuity)
            messagebox.showinfo('Monthly Payment', 'Monthly Payment is '+ u'\u20B9' +str(mp))
        def quit50():
            monthly.destroy()
        quit10 = tk.CTkButton(master=monthly, text='Quit', command=quit50, text_color="white",hover= True, hover_color= "#1a592b",border_width=2, border_color='#1a592b' ,corner_radius=20, bg_color="#262626",fg_color=None)
        quit10.grid(row=3, column=1)
        submi = tk.CTkButton(master=monthly, text='Submit', command=submit, text_color="white",hover= True, hover_color= "#1a592b",border_width=2, border_color='#1a592b' ,corner_radius=20, bg_color="#262626",fg_color=None)
        submi.grid(row=3, column=0)
    def principal():
        princi = tk.CTkToplevel(new)
        princi.title('Loan principal')
        label = tk.CTkLabel(master=princi, text='Annuity principal')
        label1 = tk.CTkLabel(master=princi, text='No. of periods')
        label2 = tk.CTkLabel(master=princi, text='Loan Interest')
        entry = tk.CTkEntry(master=princi, textvariable=tk.IntVar())
        entry1 = tk.CTkEntry(master=princi, textvariable=tk.IntVar())
        entry2 = tk.CTkEntry(master=princi, textvariable=tk.StringVar())
        label.grid(row=0, column=0)
        label1.grid(row=1, column=0)
        label2.grid(row=2, column=0)
        entry.grid(row=0, column=1)
        entry1.grid(row=1, column=1)
        entry2.grid(row=2, column=1)
        def submit():
            mp = float(entry.get())
            np = float(entry1.get())
            ir = float(entry2.get())
            i = ir/(12*100)
            principa = mp/((i*(1+i)**np)/((1+i)**np-1))
            realprincipa = round(principa)
            messagebox.showinfo('Loan principal', 'Loan principal is '+ u'\u20B9' +str(realprincipa))
        def quit50():
            princi.destroy()
        quit10 = tk.CTkButton(master=princi, text='Quit', command=quit50, text_color="white",hover= True, hover_color= "#1a592b",border_width=2, border_color='#1a592b' ,corner_radius=20, bg_color="#262626",fg_color=None)
        quit10.grid(row=3, column=1)
        submi = tk.CTkButton(master=princi, text='Submit', command=submit, text_color="white",hover= True, hover_color= "#1a592b",border_width=2, border_color='#1a592b' ,corner_radius=20, bg_color="#262626",fg_color=None)
        submi.grid(row=3, column=0)
    button = tk.CTkButton(master=new, text='Loan free by', command=loanpayoff,text_color="white",hover= True, hover_color= "#484876",border_width=2, border_color='#484876' ,corner_radius=20, bg_color="#262626",fg_color=None)
    button1 = tk.CTkButton(master=new, text='Annuity monthly payment amount', command=monthlypayment,text_color="white",hover= True, hover_color= "#484876",border_width=2, border_color='#484876' ,corner_radius=20, bg_color="#262626",fg_color=None )
    button2 = tk.CTkButton(master=new, text='Loan principal', command=principal,text_color="white",hover= True, hover_color= "#484876",border_width=2, border_color='#484876' ,corner_radius=20, bg_color="#262626",fg_color=None )
    def quitnew():
        new.destroy()
    button3 = tk.CTkButton(master=new, text='Quit', command=quitnew,text_color="white",hover= True, hover_color= "#484876",border_width=2, border_color='#484876' ,corner_radius=20, bg_color="#262626",fg_color=None)
    button.place(x=0, y=0)
    button1.place(x=0, y=40)
    button2.place(x=0, y=80)
    button3.place(x=0, y=120)
with open('Check.txt', 'r') as f:
    x = f.readlines()
    if x == []:
        button = tk.CTkButton(master=root,
         text='Enter total amount',
          command=totalamount, text_color="white",
          hover= True, hover_color= "#1f6aa5",
          border_width=2, border_color='#1f6aa5', 
          corner_radius=20, 
          bg_color="#262626",
          fg_color=None)
        button.place(x=60, y=0)
        button1 = tk.CTkButton(master=root,
         text='Enter deatils', 
         command=create, text_color="white",
         hover= True, hover_color= "#1f6aa5",
         border_width=2, border_color='#1f6aa5' ,
         corner_radius=20, 
         bg_color="#262626",
         fg_color=None)
        button1.place(x=60, y=40)
        button2 = tk.CTkButton(master=root, 
        text='Display', 
        command=display, 
        text_color="white",
        hover= True, 
        hover_color= "#1f6aa5",
        border_width=2, 
        border_color='#1f6aa5' ,
        corner_radius=20, 
        bg_color="#262626",
        fg_color=None)
        button2.place(x=400, y=40)
        button3 = tk.CTkButton(master=root, 
        text='Expense of that day', 
        command=report1, text_color="white",
        hover= True, hover_color= "#1f6aa5",
        border_width=2, 
        border_color='#1f6aa5' ,
        corner_radius=20,
        bg_color="#262626",
        fg_color=None)
        button3.place(x=640, y=40)
        button4 = tk.CTkButton(master=root, 
        text='Graphical representation of expenses of that month', 
        command=pie_chart, 
        text_color="white",
        hover= True, 
        hover_color= "#1f6aa5",
        border_width=2, 
        border_color='#1f6aa5' ,
        corner_radius=20, 
        bg_color="#262626",
        fg_color=None)
        button4.place(x=0, y=80)
        button6 = tk.CTkButton(master=root, 
        text='Income vs Expense graph of the year', 
        command=incomevsspending, 
        text_color="white",
        hover= True, 
        hover_color= "#1f6aa5",
        border_width=2, 
        border_color='#1f6aa5' ,
        corner_radius=20, 
        bg_color="#262626",
        fg_color=None)
        button6.place(x=350, y=80)
        button7 = tk.CTkButton(master=root, 
        text='Loan calculator', 
        command=debt, 
        text_color="white",
        hover= True, 
        hover_color= "#1f6aa5",
        border_width=2, 
        border_color='#1f6aa5' ,
        corner_radius=20, 
        bg_color="#262626",
        fg_color=None)
        button7.place(x=650, y=80)
        button8 = tk.CTkButton(master=root, 
        text='Quit', 
        command=quit, 
        text_color="white",
        hover= True, 
        hover_color= "#1f6aa5",
        border_width=2, 
        border_color='#1f6aa5' ,
        corner_radius=20, 
        bg_color="#262626",
        fg_color=None)
        button8.place(x=400, y=240)
    else:
        button1 = tk.CTkButton(master=root, 
        text='Enter deatils', 
        command=create, 
        text_color="white",
        hover= True, 
        hover_color= "#1f6aa5",
        border_width=2, 
        border_color='#1f6aa5' ,
        corner_radius=20, 
        bg_color="#262626",
        fg_color=None)
        button1.place(x=60, y=0)
        button2 = tk.CTkButton(master=root, 
        text='Display', 
        command=display, 
        text_color="white",
        hover= True, 
        hover_color= "#1f6aa5",
        border_width=2, 
        border_color='#1f6aa5' ,
        corner_radius=20, 
        bg_color="#262626",
        fg_color=None)
        button2.place(x=400, y=0)
        button3 = tk.CTkButton(master=root, 
        text='Expense of that day', 
        command=report1, 
        text_color="white",
        hover= True, 
        hover_color= "#1f6aa5",
        border_width=2, 
        border_color='#1f6aa5' ,
        corner_radius=20, 
        bg_color="#262626",
        fg_color=None)
        button3.place(x=640, y=0)
        button4 = tk.CTkButton(master=root, 
        text='Graphical representation of expenses of that month', 
        command=pie_chart, 
        text_color="white",
        hover= True, 
        hover_color= "#1f6aa5",
        border_width=2, 
        border_color='#1f6aa5' ,
        corner_radius=20, 
        bg_color="#262626",
        fg_color=None)
        button4.place(x=0, y=40)
        button6 = tk.CTkButton(master=root, 
        text='Income vs Expense graph of the year', 
        command=incomevsspending, 
        text_color="white",
        hover= True, 
        hover_color= "#1f6aa5",
        border_width=2, 
        border_color='#1f6aa5' ,
        corner_radius=20, 
        bg_color="#262626",
        fg_color=None)
        button6.place(x=350, y=40)
        button7 = tk.CTkButton(master=root, 
        text='Loan calculator', 
        command=debt, 
        text_color="white",
        hover= True, 
        hover_color= "#1f6aa5",
        border_width=2, 
        border_color='#1f6aa5' ,
        corner_radius=20, 
        bg_color="#262626",
        fg_color=None)
        button7.place(x=650, y=40)
        button8 = tk.CTkButton(master=root, 
        text='Quit', 
        command=quit, 
        text_color="white",
        hover= True, 
        hover_color= "#1f6aa5",
        border_width=2, 
        border_color='#1f6aa5' ,
        corner_radius=20, 
        bg_color="#262626",
        fg_color=None)
        button8.place(x=400 , y=240)
label1 = tk.CTkLabel(master=root, text='Financial tips:')
label1.place(x=400, y=120)
label2 = tk.CTkLabel(master=root, text='1.Create A Budget \n2.Use Cash Instead Of Plastic Money \n3.Create An Emergency Fund \n4.Avoid Taking On Debt \n5.Start Investing')
label2.place(x=370, y=140)
root.mainloop()