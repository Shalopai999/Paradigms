num = int(input("Введите число: "))
if num < 1:
    print("Введите положительное число!")
else:
    for count in range(1, 10):
        print(num, " * ", count, " = ", num * count)