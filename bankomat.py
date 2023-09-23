def start_menu(account_balance):
    count_operation = 0
    percent_operation = 0.03
    wealth_tax = 0.1
    while True:
        print("")
        print("Главное меню!!!")
        if account_balance > 5_000_000:
            account_balance = round(account_balance - account_balance*wealth_tax, 2)
        print(f"Баланс Вашего счета - {account_balance}")
        operation_number = input("Выберите операцию!!!\n"
                                 "1 - Пополнение\n"
                                 "2 - Снятие\n"
                                 "3 - Выход\n").strip()
        match operation_number:
            case "1":
                account_balance = replenishment_operation(account_balance)
                count_operation += 1
                if count_operation == 3:
                    account_balance = account_balance + round(account_balance*percent_operation, 2)
                    count_operation = 0
            case "2":
                account_balance = withdrawal_operation(account_balance)
                count_operation += 1
                if count_operation == 3:
                    account_balance = account_balance + round(account_balance * percent_operation, 2)
                    count_operation = 0
            case "3":
                exit()
            case _:
                print("Некорректный выбор!!!! Повторите выбор")


def replenishment_operation(account_balance):

    while True:
        deposit_amount = int(input("Введите сумму пополнеия кратную 50 у.е.: "))
        if deposit_amount % 50 == 0:
            account_balance = account_balance + deposit_amount
            return account_balance
        else:
            print("Вы ввели некорректную сумму!!!!  Повторите ввод!!!!")


def withdrawal_operation(account_balance):
    percent_withdrawal = 0.015
    min_sum = 30
    max_sum = 600
    while True:
        withdrawal_amount = int(input("Введите сумму снятия кратную 50 у.е.: "))
        if withdrawal_amount % 50 == 0:
            if withdrawal_amount > account_balance:
                print("На счете недостаточно денег!!!!!")
            else:
                if withdrawal_amount*percent_withdrawal < min_sum:
                    account_balance = account_balance - withdrawal_amount - min_sum
                    return account_balance
                elif withdrawal_amount*percent_withdrawal > max_sum:
                    account_balance = account_balance - withdrawal_amount - max_sum
                    return account_balance
                else:
                    account_balance = account_balance - withdrawal_amount - withdrawal_amount*percent_withdrawal
                    return account_balance
        else:
            print("Вы ввели некорректную сумму!!!!  Повторите ввод!!!!")


start_menu(account_balance=0)