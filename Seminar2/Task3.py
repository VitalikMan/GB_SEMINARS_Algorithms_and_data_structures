# # Код от Ильи Медянкина
# from random import randint
# from time import time
#
# import lst as lst
#
#
# def list_gen(mi=-5, ma=5, le=10):
#  return [randint(mi, ma) for i in range(le)]
#
#
# # bubble_sort
# def algo_time(func, x):
#     start = time()
#     func(x)
#     finish = time() - start
#     print(f'Выполнение за {finish} сек.')
#
#
# def bubble_sort(lst):
#     for i in range(len(lst)):
#         for j in range(len(lst) - 1 - i):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     return lst
#
#
# def quick_sort(lst):
#     if len(lst) <= 1:
#         return lst
#     pivot = lst[len(lst) // 2]
#     left = list(filter(lambda x: x < pivot, lst))
#     center = [i for i in lst if i == pivot]
#     right = list(filter(lambda x: x > pivot, lst))
#     return quick_sort(left) + center  +quick_sort(right)
#
#
# def binary_search(lst, value, left, right):
#     if right < left:
#         return None
#     middle_point = (right - left) // 2 + left
#     if lst[middle_point] < value:
#         return binary_search(lst, value, middle_point + 1, right)
#     elif lst[middle_point] > value:
#         return binary_search(lst, value, left, middle_point - 1)
#     else:
#         return middle_point
#
# my_list = list_gen(-100, 100, 1_000_000)
# # algo_time(bubble_sort, my_list)
# # print(my_list)
# start = time()
# my_list.sort()
# finish = time() - start
# # print(my_list)
# print(f'Выполнение за {finish} сек.')
#
# print('-' * 50)
#
# my_list = list_gen(-10, 10, 20)
# # print(my_list)
# start2 = time()
# my_list_sorted = quick_sort(my_list)
# finish2 = time() - start
# print(my_list_sorted)
# print(f'Выполнение за {finish2} сек.')
#
# print('-' * 50)
#
# start3 = time()
# value_to_search = 0
# result_of_binary_search = binary_search(my_list_sorted, value_to_search, 0, len(my_list_sorted)-1)
# finish3 = time() - start
# # print(f'Искомое число {my_list_sorted} ')
# print(f'{result_of_binary_search}')
# print(f'Выполнение за {finish3} сек.')
#
#
#
# # Дополнительный код
# from random import randint
#
#
# def bubble(sp):
#     start = time.time()
#     for i in range(len(sp)-1):
#         for j in range(len(sp)-i-1):
#             if sp[j] > sp[j+1]:
#                 sp[j], sp[j+1] = sp[j+1],sp[j]
#
#     print(sp)
#     print(time.time() - start)
#
# def counting_sort(sp):
#     start = time.time()
#     max_item = max(sp)
#     lst=[0 for _ in range(max_item+1)]
#     for i in sp:
#         lst[i]=lst[i]+1
#     print(lst)
#     index = 0
#  # for i in range(len(lst)):
#  # for j in range(lst[i]):
#  # sp[index]=i
#  # index+=1
#  res_sp = []
#  for i in range(len(lst)):
#     if lst[i]:
#         res_sp.extend([i] * lst[i])
#  print(res_sp)
#  print(time.time() - start)
#
# print(sp := [randint(0, 10) for _ in range(20)])
# bubble(sp)
# counting_sort(sp)
