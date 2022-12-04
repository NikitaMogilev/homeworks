#алгоритм
# 1. бесконечный уикл
# 2. Пользователь должен ввести номер телефона
# 3. Спрашивать пользователя хочет ли он выйти
## 4. Провалидировать номер согласно ТЗ
# 5. Если валидация не успешна вывеси ошибку
#6.если валидация успешна вывести даные
#
from itertools import chain

operators_codes = {'25':'life','291':'a1', '293':'a1','296':'a1', 
                    '299':'a1','44':'a1', '292':'mts','295':'mts', 
                    '297':'mts','298' : 'mts', '33':'mts'}

while True:
    result = {}
    user_input = input('Введите номер телефона:  ')
    error = False
    
    
    if len(user_input) != 13:
        result['success'] = False
        result['desription'] = 'Phone number should contains 13 symbols'
        #print(result)
        error = True
        
    
    for symbol in user_input[1:]:
        if not symbol.isdigit():
            result['success'] = False
            result['desription'] = 'Phone number should contains only digits'
            #print(result)
            error = True
            break
    
    if user_input[0] != "+":
        result['success'] = False
        result['desription'] = 'First symbol shoul be "+" '
       # print(result)
        error = True
        

    if user_input[1:4] != "375":
        result['success'] = False
        result['desription'] = 'Unknown country code'
       # print(result)
        error = True  
        
    
    if user_input[4:7] not in operators_codes.keys():
        if user_input[4:6] not in operators_codes.keys():
            result['success'] = False
            result['desription'] = 'Unknown operator'
            error = True
    
    if error:
        print(result)
    else:
        result['success'] = True
        result['phone'] = user_input 
        
        if user_input[4:7]  in operators_codes.keys():
            result['desription'] = operators_codes.get(user_input[4:7])
        if user_input[4:6]  in operators_codes.keys():
            result['desription'] = operators_codes.get(user_input[4:6])

        print(result)    
        
       
    

    exit_choice = input('Хотите выйти из программы (Y/N)')
    if exit_choice == 'Y':
        break
