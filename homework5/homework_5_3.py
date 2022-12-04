user_input = input('Введите символ для поиска: ')
with open('test.txt') as my_file:
    letter_counter = 0
    for line in my_file:
        low_line = line.lower()
        for symbol in low_line:
            if user_input == symbol:
                letter_counter += 1
    print(letter_counter)
