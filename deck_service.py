import blackjack_view
    
def init(deck):
    deck.refresh_current_deck()

def draw_cards(hand, cards, deck):
    for i in range(cards):
        card = deck.current_deck.pop()
        card_cost = deck.return_card_cost(card)
        hand[card] = card_cost
    return hand

def show_2_cards(player, dealer, deck):
    player.hand = draw_cards(player.hand, 2, deck)
    player.update_value()
    dealer.hand = draw_cards(dealer.hand, 2, deck)
    dealer.update_value()
    blackjack_view.print_cards_player_turn(player, dealer)

def refresh_game(player, dealer, deck):
    deck.refresh_current_deck()
    player.hand = {}
    dealer.hand = {}
    player.value = 0
    dealer.value = 0

def take_debt(player):
    player.debt = player_take_debt()
    player.balance += player.debt

def pay_off_debt(player):
    player.balance -= player.debt
    player.debt = 0

def charging_interest(player):
    player.debt *= 1.15
    player.debt = round(player.debt)

def bet_validation(player):
    bet = 0
    while bet <= 0 or bet > player.balance:
        try:
            bet = int(input('Введи сумму ставки: '))
            if bet > player.balance:
                raise Exception('\nСтавка превышает размер баланса!')
            if bet <= 0:
                raise Exception('\nРазмер ставки должен быть положительным числом!')
        except ValueError:
            print('\nДолжно быть введено число!')
        except Exception as errors:
            print(f'{errors.args[0]}')    
    return bet

def player_choice(str):
    choice = ''
    while choice != 'y' and choice != 'n':
        try:
            choice = input(str)
            if choice != 'y' and choice != 'n':
                raise Exception('\nНеобходимо ввести "y" или "n"')
        except Exception:
            print('\nНеобходимо ввести "y" или "n"')  
    return choice

def player_take_debt():
    debt = 0
    while debt <= 0 or debt > 2000:
        try:
            debt = int(input('\nВведи сумму займа (до 2000 х.к.): '))
            if debt > 2000:
                raise Exception('\nСумма займа не должна превышать 2000 х.к.!')
            if debt <= 0:
                raise Exception('\nСумма займа должна быть положительным числом!')
        except ValueError:
            print('\nДолжно быть введено число!')
        except Exception as errors:
            print(f'{errors.args[0]}')    
    return debt