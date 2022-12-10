def get_winner(*point_of_gamers):
    board_of_gamers = []
    for index, gamers in enumerate(points_of_gamers):
        list_of_gamers = gamers, index+1
        board_of_gamers.append(list_of_gamers)
    sort_gamers = sorted(board_of_gamers, reverse=True)
    winners = sort_gamers[0:3]
    number_of_winner = [number_of_winner[1] for number_of_winner in winners]
    return number_of_winner


points_of_gamers = [599, 67, 94, 87, 6, 44]
# Вариант если очки игроков вводить с консоли
# points_of_gamers = list(map(int, input('Введите очки\
#  игроков от 0 до 600 через пробел\
#  и нажмите Enter ').split(' ')))
winners = get_winner(points_of_gamers)
print(f'Номера победителей {winners}')
