import time

def hello():
     print('\nНу привет новеньй (старенький?). Ты показал неплохие результаты в умении рассказывать анекдоты.')
     print('Однако тебя ждет следующее испытание: сыграть в очко с паханом.')
     print('На старте твой банк составляет 1000 хлебных крошек (х.к.). Твоя цель заключается в наборе 3000 х.к.')
     print('Знай, если сильно проиграешься, то ты можешь залезть в долги. Тебе будет предложено взять до 2000 дополнительных х.к.')
     print('Долг платежом красен, а потому у тебя будут накапливаться проценты по задолженности (15 %) после каждой сыгранной партии.')
     print('Проценты будут начисляться до тех пор, пока долг не будешь погашен. Ты не сможешь одержать победу, пока не выплатишь свой долг.')
     print('При достижении величины долга свыше 3000 х.к., ты проиграешь')

def print_player_draw_card():
    time.sleep(0.5)
    print('\nТы вытягиваешь карту...')

def print_dealer_draw_card():
    time.sleep(0.5)
    print('\nКрупье вытягивает карту...')

def print_cards_player_turn(player, dealer):
    print()
    print('Карты игрока: ', end='')
    time.sleep(0.5)
    print(', '.join([str(key) for key in player.hand.keys()]) + f'. (Сумма очков: {player.value})')
    print('Карты крупье: ', end='')
    time.sleep(0.5)
    print(f'{list(dealer.hand)[0]}, ***' + f'. (Сумма очков: ***)')
    time.sleep(0.5)

def print_cards_dealer_turn(player, dealer):
    print()
    print('Карты игрока: ', end='')
    time.sleep(0.5)
    print(', '.join([str(key) for key in player.hand.keys()]) + f'. (Сумма очков: {player.value})')
    print('Карты крупье: ', end='')
    time.sleep(0.5)
    print(', '.join([str(key) for key in dealer.hand.keys()]) + f'. (Сумма очков: {dealer.value})')
    time.sleep(0.5)