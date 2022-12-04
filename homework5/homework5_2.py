user_index = int(input('Введите индекс:'))

a = 0
b = 1
index = 1
while True:
    index += 1
    next_number = a + b
    a = b
    b = next_number

    if user_index == index:
        print(f'число по заданному индексу {index} = {next_number}')
        break
    
    if user_index == 1:
        print('число по заданному индексу 1 = 1')
        break
    
    if user_index == 0:
        print('число по заданному индексу 0 = 0')
        break
