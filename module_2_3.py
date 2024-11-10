my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print('Список', my_list, '\nПоложительные числа из списка:')

start = 0
while start < len(my_list):

    num = my_list[start]  
    start = start + 1  

    if num == 0:
        continue  

    elif num < 0:
        print('Встретилось отрицательное число:', num)
        break

    else:
        print(num)
