#found = 0
# def binary_search(list, item):
#     global found
#     low = 0
#     high = len(list) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         guess = list[mid]
#         if guess == item:
#             print('Found at',mid+, 'position')
#             found = 1
#
#
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#
# list = eval(input('Enter no: '))
# item = int(input('Enter no: '))
#if found == 0:
#   print('Not found')
# def bubblesort(list):
#     for i in range(len(list)):
#         for j in range(0,len(list)-i-1):
#             if list[j]>list[j+1]:
#                 list[j],list[j+1] = list[j+1], list[j]
#     print(list)
# def insertionsort(list):
#     for i in range(1,len(list)):
#         key = list[i]
#         j=i-1
#         while j>=0 and key<list[j]:
#             list[j+1]=list[j]
#             j=j-1
#         else:
#             list[j+1] = key
#     print(list)