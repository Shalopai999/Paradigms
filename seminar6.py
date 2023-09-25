list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

num = int(input("Введите число для поиска: "))
low = 0
mid = 0

high = len(list) - 1

if num < high+2 and num > low:

    while num != mid + 1:
        mid = low + (high - low) // 2
        if list[mid] == num:
            print(f"Число {num} находится на {mid} позиции")
            break
        elif list[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
else:
    print("-1")