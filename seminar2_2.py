from fractions import Fraction

numerator_1, denominator_1 = map(int, input("Введите первую дробь через /: ").split("/"))
numerator_2, denominator_2 = map(int, input("Введите вторую дробь через /: ").split("/"))
a = Fraction(numerator_1, denominator_1)
b = Fraction(numerator_2, denominator_2)
print(a * b)
print(a + b)
print('*' * 50)


def composition(num_1, denom_1, num_2, denom_2):
    numerator = num_1 * num_2
    denominator = denom_1 * denom_2
    numerator, denominator = reduction_of_fractions(numerator, denominator)
    if numerator == denominator:
        return print(f'произведение дробей = {numerator}')
    else:
        return print(f'произведение дробей = {numerator}/{denominator}')


def sum_of_fractions(num_1, denom_1, num_2, denom_2):
    if denom_1 == denom_2:
        numerator = num_1 + num_2
        denominator = denom_1
        numerator, denominator = reduction_of_fractions(numerator, denominator)
        if numerator == denominator:
            return print(f'сумма дробей = {numerator}')
        else:
            return print(f'сумма дробей = {numerator}/{denominator}')
    else:
        numerator = (num_1 * denom_2) + (num_2 * denom_1)
        denominator = denom_1 * denom_2
        numerator, denominator = reduction_of_fractions(numerator, denominator)
        if numerator == denominator:
            return print(f'сумма дробей = {numerator}')
        else:
            return print(f'сумма дробей = {numerator}/{denominator}')


def reduction_of_fractions(num_1, num_2):
    if num_1 > num_2:
        common_denominator = num_2
    else:
        common_denominator = num_1
    for i in range(common_denominator, 1, -1):
        if num_1 % i == 0 and num_2 % i == 0:
            num_1 = int(num_1 / i)
            num_2 = int(num_2 / i)
    return num_1, num_2


composition(numerator_1, denominator_1, numerator_2, denominator_2)
sum_of_fractions(numerator_1, denominator_1, numerator_2, denominator_2)
