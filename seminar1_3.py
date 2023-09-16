from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPTS_LIMIT = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)
attempt = 1
while attempt <= ATTEMPTS_LIMIT:
    print(f"Попытка номер {attempt}")
    user_number = int(input("Введите число: "))
    if user_number == num:
        print("Победа!!!! Вы угадали число")
        break
    elif user_number < num:
        print(f"Введенное Вами число {user_number} меньше загаданного")
    else:
        print(f"Введенное Вами число {user_number} больше загаданного")
    attempt += 1
else:
    print(f"Вы проиграли. Попытки закончились. Было загадано число {num} ")