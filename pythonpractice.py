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

no=int(input('enter the no'))
s=str(no)
for i in s:
    if int(i)**3==no:
        print('armstrong no')
    else:
        print('not')
        