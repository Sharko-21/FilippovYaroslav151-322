def check_num(num):
    numbers_arr = []
    for i in range(0, num + 1):
        numbers_arr.append(True)
    numbers_arr[0] = False
    numbers_arr[1] = False
    for i in range(1, num + 1):
        if numbers_arr[i] == True:
            for j in range(i + i, num + 1, i):
                numbers_arr[j] = False
    return [i for i in range(0, num + 1) if numbers_arr[i]]


print(check_num(int(input())))