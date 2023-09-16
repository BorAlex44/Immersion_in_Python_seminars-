while True:
    user_number = int(input("Введите число в диапазоне от 1 до 100000: "))
    if user_number < 1 or user_number > 100000:
        print("вы ввели некорректное число!!!! Повторите ввод")
        continue
    else:
        break

if user_number == 1:
    print("Вы ввели число 1. Число 1 не является не простым, ни составным!!!!")
else:
    count = 0
    for i in range(1, user_number + 1):
        if user_number % i == 0:
            count += 1
    if count > 2:
        print(f"Введенное число {user_number} является составным")
    else:
        print(f"Введенное число {user_number} является простым")
