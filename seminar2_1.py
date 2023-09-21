user_number = int(input("Введите любое целое число: "))
res_str = ''
sample_list = '0123456789abcdef'
print(hex(user_number))

while user_number:
    res_str = sample_list[user_number % 16] + res_str
    user_number //= 16


print(f'0x{res_str}')
