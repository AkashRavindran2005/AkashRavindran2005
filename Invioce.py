import csv
from datetime import date
today=date.today()
with open('Invoice.csv','w',newline='') as f:
    sr=csv.writer(f)
    s=[
        ['                          AK STORE                      '],
        ['                     A.G.s Colony, Nanganallur'],
        ['                         chennai-66'],

        ['Date:',today,'Invoice no.:']
    ]
    sr.writerows(s)
with open('Invoice.csv','r',newline='') as f1:
    sw=csv.reader(f1)
    for i in sw:
        print(i)




