def get_numbers(first_num, second_num):
    if (first_num < 0):
        return 'Число не может быть меньше 0'
    if (second_num <= first_num):
        return 'Числа должны быть разными!'

    arr = []

    for i in range(first_num, second_num):
        if(i == 0):
            continue

        if (i % 5 == 0):
            arr.append(i)

    return arr


print(get_numbers(int(input('Введите первое число: ')), int(input('Введите второе число: '))))
