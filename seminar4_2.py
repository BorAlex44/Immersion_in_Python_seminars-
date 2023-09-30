def my_dict_result(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        try:
            result_dict[value] = key
        except TypeError:
            result_dict[str(value)] = key
    return result_dict


print(my_dict_result(name='Sasha', age=45, address=['Kostroma', 'Kostromskay street'], height=175.5, flag=True))