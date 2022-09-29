# import pickle
# s=[]
# with open('member.dat','wb') as f:
#     while True:
#         no=int(input('enter member no'))
#         name=input('enter name')
#         s.append([no,name])
#         ch=input('press y to continue')
#         if ch!='y':
#             break
#     pickle.dump(s,f)
import pickle

# num=int(input('enter member code'))
# with open('member.dat','rb') as f:
#     try:
#         while True:
#             x=pickle.load(f)
#             for i in x:
#                 if i[0]==num:
#                     print('member no',i[0],'member name',i[1])
#     except EOFError:
#         print('')

# l1=eval(input('enter the list'))
# n=int(input('enter the number to be searched'))
# l=0
# print(len(l1))
# u=len(l1)-1
# pos=0
# def binaryfuckery(l1,n,l,u):
#     while True:
#         mid=(l+u)//2
#         if l1[mid]==n:
#             global pos
#             pos+=mid
#             return True
#         elif l1[mid]>n:
#             u=mid-1
#         elif l1[mid]<n:
#             l=mid+1
#     return False
# if binaryfuckery(l1,n,l,u):
#     print('found at',pos)
# else:
#     print('not found')

# l=eval(input('enter the list: '))
# l1=len(l)
# for i in range(l1):
#     for j in range(0,l1-i-1):
#         if l[j]<l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

# l=eval(input('enter the list: '))
# n=len(l)
# for i in range(1,n):
#     key=l[i]
#     j=i-1
#     while j>=0 and key>l[j]:
#         l[j+1]=l[j]
#         j=j-1
#     else:
#         l[j+1]=key
# print(l)

# no=int(input('enter the no'))
# s=str(no)
# for i in s:
#     if int(i)**3==no:
#         print('armstrong no')
#     else:
#         print('not')

# with open('para.txt','r') as f:
#     f1=open('stu.txt','w')
#     c=0
#     z=f.readlines()
#     vowels='AEIOUaeiou'
#     x=f.read()
#     a=x.split()
#     print(len(a))
#     print(a.count('is'))
#     for i in a:
#         for j in i:
#             if j in vowels:
#                 c+=1
#     print(c)
#     for i in z:
#         if 'p' in i:
#             f1.write(i)
#
# import pickle
# s=[]
# with open('para.dat','wb') as f:
#     while True:
#         bno=int(input('enter book no'))
#         bname=input('enter name')
#         aname=input('enter author name')
#         bgenre=input('enter genre')
#         s.append([bno,bname,aname,bgenre])
#         ch=input('enter y to continue')
#         if ch!='y':
#             break
#     pickle.dump(s,f)
# n=int(input('enter book no'))
# with open('para.dat','rb') as f:
#     try:
#         while True:
#             x=pickle.load(f)
#             for i in x:
#                 if i[0]==n:
#                     print(i)
#             print(x)
#     except EOFError:
#         print('')

# with open('para.txt','r') as f:
#     data=f.readlines()
#     print(data)

# i=0
# while i<6:
#     j=0
#     while j<1:
#         print('*',end=' ')
#         j=j+1
#     i=i+1
#     print( )
#
# x=7
# y=8
# if x<7 or x<=10 and y>8:
#     print('IT IS!')
# else:
#     print('Oh No')
#
# score=40
# while score>1:
#     score=score/2-1
#     print(score,end=' ')
#
# for i in range(0,101):
#     print (i,'\t|',((i-32)*5)/9)

# a='blueberry'
# vowels='aeiouAEIOU'
# str=''
# for i in a:
#     if i in vowels:
#         str=str+'('+i+')
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# a=dict.fromkeys(a)
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# b=dict.fromkeys(b)
# l=[]
# for i in a:
#     for j in b:
#         if i==j:
#             l.append(i)
# print(l)

# with open('para.txt','r') as f:
#     l=[]
#     x=f.read()
#     a=x.split()
#     for i in a:
#         for j in a:
#             for k in j:
#                 l.append((k,x.count(k)))
#     t=dict.fromkeys(l)
#     s=list(t)
#     for m in s:
#         print('no. of',m[0],'is',m[1])
import pickle

# n=int(input('enter book id'))
# l=[]
# found=False
# with open('para.dat','rb+') as f:
#     try:
#         while True:
#             f.seek(0)
#             rpos=f.tell()
#             l=pickle.load(f)
#             for i in l:
#                 if i[0]==n:
#                     ch=input('do you want to modify? if yes press "y"')
#                     if ch=='y':
#                         n1=input('enter name')
#                         l.append(n1)
#                         f.seek(rpos)
#                         pickle.dump(l,f)
#                         found=True
#                     else:
#                         break
#     except EOFError:
#         if found==False:
#             print('no matching records found')
#         else:
#             print('done!')
# import csv
# def write():
#     with open('para.csv','w',newline = '') as f:
#         sw = csv.writer(f)
#         while True:
#             rno=int(input('enter: '))
#             name=input('enter: ')
#             marks=int(input('enter: '))
#             rec=[rno,name,marks]
#             sw.writerow(rec)
#             ch=input('y to continue')
#             if ch!='y':
#                 break
# def read():
#     with open('para.csv','r',newline='') as f:
#         sw=csv.reader(f)
#         for i in sw:
#             print(i)
#
# def update():
#     with open('para.csv','r+') as f:
#         n=int(input("Enter: "))
#         sw=csv.writer(f)
#         sr=csv.reader(f)
#         pos=f.tell()
#         for i in sr:
#             if i[0]==n:
#                 m=int(input('enter: '))
#                 i[2]=m
#                 f.seek(pos)
#                 sw.writerow(sr)
#
# write()
# read()
# update()
# read()

# s=[1,2,3,4,5,6]
# # while len(s)>0:
# #     print(s.pop())
# x=len(s)-1
# while x>=0:
#     print(s[x])
#     x=x-1


list = [23, 1, 31, 106, 3]
# n=int(input('enter no: '))
# u=len(list)-1
# l=0
# flag=0
# while len(list)>=0 and flag==0:
#     m=(l+u)//2
#     if list[m]==n:
#         print('found at',m+1,'th position')
#         flag+=1
#     elif list[m]>n:
#         u=m-1
#     elif list[m]<n:
#         l=m+1
# if flag==0:
#         print('not found')

# n=len(list)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if list[j]>list[j+1]:
#             list[j],list[j+1]=list[j+1],list[j]
# print(list)
#
# for i in range(1,n):
#     key=list[i]
#     j=i-1
#     while j>=0 and list[j]>key:
#         list[j+1]=list[j]
#         j=j-1
#     else:
#         list[j+1]=key
# print(list)

# def matrix():
#     m=int(input('enter row: '))
#     n=int(input('enter columns: '))
#     mat=[]
#     for i in range(m):
#         r=[]
#         for j in range(n):
#             no=int(input("enter element: "))
#             r.append(no)
#         mat.append(r)
#     return mat
# x=matrix()
# def check1(x):
#     r=[]
#     for i in range(len(x)):
#         no_of1=0
#         for j in range(len(x[0])):
#             if x[i][j]==1:
#                 no_of1+=1
#         r.append(no_of1)
#     print('no of ones',max(r),'is in',r.index(max(r))+1,'nth line')
# check1(x)
# def unique(x):
#     r=[]
#     for i in range(len(x)):
#         k=x[i]
#         for j in range(len(x[0])):
#             r.append(x[i][j])
#     for f in r:
#         if r.count(f)==1:
#             print(f)
# s=[]
# def isempty():
#     if s==[]:
#         return True
#     else:
#         return False
#
# def push(s,item):
#     for i in item:
#         s.append(i)
# def pop(s):
#     if isempty():
#         print("underflow")
#     else:
#         x=len(s)-1
#         str=''
#         while x>=0:
#             f=s.pop(x)
#             str+=f
#             x=x-1
#         print(str)
# def display(s):
#     if isempty():
#         print('Undderflow')
#     else:
#         x=len(s)-1
#         while x>=0:
#             print(s[x])
#             x=x-1
# item=input('enter')
# push(s,item)
# pop(s)
# display(s)
# import pickle
# def write():
#     with open('student.dat','wb') as f:
#         while True:
#             rno=int(input("enter roll no: "))
#             name=input("enter name: ")
#             marks=int(input("enter marks: "))
#             rec=[rno,name,marks]
#             pickle.dump(rec, f)
#             ch=input('enter y to continue')
#             if ch!='y':
#                 break
#
# def update():
#     with open('student.dat','rb+') as f:
#         rno=int(input("enter roll no you want to change: "))
#         try:
#             flag=0
#             while True:
#                 r=f.tell()
#                 x=pickle.load(f)
#                 if rno==x[0]:
#                     marks=int(input("enter marks: "))
#                     x[2]=marks
#                     f.seek(r)
#                     pickle.dump(x,f)
#                     flag=1
#             if flag==0:
#                 print('not found')
#
#         except EOFError:
#             print('')
# def read():
#     with open('student.dat','rb') as f:
#         try:
#             while True:
#                 x=pickle.load(f)
#                 print(x)
#         except EOFError:
#             print('')

# with open('story.txt','w') as f:
#     while True:
#         x=eval(input("Enter a line as list: "))
#         f.writelines(x)
#         ch=input('Enter "y" to continue: ')
#         if ch!='y':
#             break
# with open('story.txt','r') as f:
#     flag=0
#     r=f.readlines()
#     a=0
#     d=0
#     s=0
#     for i in range(len(r)):
#         for j in r:
#             for k in x[i]:
#                 for l in j:
#                     if l.isalpha():
#                         print('No. of alphabet in',i+1,'th line is',j.count(k))

# x=100 or 200
# p)
# rint(x
# s=[]
# def isempty(s):
#     if s==[]:
#         return True
#     else:
#         return False
# def push(s,year):
#     s.append(year)
# def pop(s):
#     if isempty(s):
#         print("Underflow")
#     else:
#         x=len(s)-1
#         while x>=0:
#             print(s.pop(x))
#             x=x-1
#
# while True:
#     print('1.push')
#     print('2.pop')
#     ch=int(input('Enter choice'))
#     if ch==1:
#         year=int(input('Enter year'))
#         push(s,year)
#     elif ch==2:
#         pop(s)
#     else:
#         break
# print(u'\u20B9')

# T = eval(input('Enter tuple: '))
# r = []
# for i in T:
#     r.append(len(i))
# print(tuple(r))
# l = []

# while True:
#     date = input('enter: ')
#     def append(l,date):
#         global no
#         for i in l:
#             if i == date:
#                 no += 1
#             elif i != date:
#                 no = 0
#         return no
#     l.append(date)
#     ch=input("Enter: ")
#     if ch=='y':
#         no=0
#         print(append(l,date))
#     else:
#         break

# l=[1,2]
# m=[3,4]
# n=[5,6]
# o=[]
# o.extend(l)
# o.extend(m)
# o.extend(n)
# print(o)

# import csv
# def check():
#     with open('notes1.csv','w',newline='') as f1:
#         with open('notes.csv', 'r', newline='') as f:
#             sr = csv.reader(f)
#             sw=csv.writer(f1)
#             for i in sr:
#                 if i[0][:5] != 'check':
#                     sw.writerow(i)
# check()
#
# for i in range(1,100):
#     if 10 <= i < 100:
#         print(i)

# d = [["Mark", 12, 95],
#      ["Jay", 11, 88],
#      ["Jack", 14, 90]]
#
# print("{:<8} {:<8} {:<8}".format('Name', 'Age', 'Percent'))
#
# for v in d:
#     name, age, perc = v
#     print("{:<8} {:<8} {:<8}".format(name, age, perc))
#
# header = [re.sub(' +',' ',i[0][:-1].replace('\n', ' ')) for i in optionsTable[0]]
#
# with open('test.csv', 'w') as fp:
#    writer = csv.writer(fp, delimiter=',')
#    writer.writerow(header)
#    for row in optionsTable:
#       writer.writerow([i[1] for i in row])
# import pickle
# with open('products.dat', 'rb+') as f1:
#     try:
#         while True:
#             x = pickle.load(f1)
#             print(x)
#     except EOFError:
#         print('')
# import csv
# with open('products.csv', 'r', newline='') as f1:
#     reader = csv.reader(f1)
#     print('{:<60} {:<5}'.format('Products', 'Stocks'))
#     found = 0
#     n = []
#     for i in reader:
#         print('{:<60} {:<5}'.format(i[0], i[1]))
#         key = i
#
#
#     def check(product, reader, quantity):
#         global found
#         global n
#         f1.seek(0)
#         for rec in reader:
#             if rec[0].lower() == product.lower():
#                 rec[1] = str(int(rec[1]) - quantity)
#                 found = 1
#                 n.append(rec)
#                 return True
#             else:
#                 return False
#
#
#     product = input('Enter Product name: ')
#     quantity = int(input("Enter quantity: "))
#     for rec in range(len(reader)):
#         print(rec)
#         if reader[rec][0].lower() == product.lower():
#             rec[1] = str(int(rec[1]) - quantity)
#             found = 1
#             n.append(rec)
#             print(n)
#     if found == 0:
#         print('not found')
# import tkinter
# root = tkinter.Tk()
# def bruh():
#     label = tkinter.Label(root,text='ok')
#     label.pack()
# start = tkinter.Button(root, text= 'start', command=bruh)
# start.pack()
# root.mainloop()
# import tkinter
# root = tkinter.Tk()
# label = tkinter.Label(root,text='Akash')
# label.pack()
# root.mainloop()
