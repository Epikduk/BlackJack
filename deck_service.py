import random
import deck_reader as reader
import blackjack_view

deck = {}
current_deck = {}

def init():
    global deck
    deck = reader.read_deck()
    refresh_current_deck()

def draw_cards(hand, cards):
    global current_deck
    draw_cards = random.sample(sorted(current_deck), k = cards)
    delete_cards(current_deck, draw_cards)
    for card in draw_cards:
        hand[card] = deck[card]
    return hand

def delete_cards(current_deck, draw_cards):
    for card in draw_cards:
        del current_deck[card]    

def refresh_current_deck():
    global current_deck
    current_deck = deck.copy()

def show_2_cards(player, dealer):
    player.draw_2_cards()
    dealer.draw_2_cards()
    blackjack_view.print_cards_player_turn(player, dealer)

def refresh_game(player, dealer):
    refresh_current_deck()
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