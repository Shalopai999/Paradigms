list1 = [5, 1, 8, 0, 3, 7, 2, 4, 6]
print(f'Изначальный список №1: {list1}')
list1.sort(reverse = True)
print(f'Декларативный способ, сортировка по убыванию списка №1: {list1}')

list2 = [4, 1, 8, 3, 0, 9, 5]
print(f'Изначальный список №2: {list2}')
n = True
while n:
    n = False
    for i in range(len(list2) - 1):
        if list2[i] < list2[i + 1]:
            list2[i], list2[i + 1] = list2[i + 1], list2[i]
            n = True
print(f'Императивный способ, сортировка по убыванию списка №2: {list2}')