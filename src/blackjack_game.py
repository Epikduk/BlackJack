import src.deck_service as deck_service
import src.blackjack_view as blackjack_view
import entities
import time

def main():
    blackjack_view.hello()
    deck = entities.Deck()
    deck_service.init(deck)
    player = entities.Player()
    dealer = entities.Dealer()
    status = True
    while status:
        start_game(player, dealer, deck)
        if player.debt > 3000:
            print('\nЭто конечная.. Сейчас кого-то будут убивать.')
            status = False
        if player.balance >= player.debt and player.debt > 0:
            pay_off_debt(player)
        elif player.balance == 0 and player.debt == 0:
            debt_offer(player)
        elif player.balance >= 3000 and player.debt == 0:
            print('\nПоздравляю, малой! Ты успешно справился со своей задачей! Увидимся в следующей части серии')
            status = False
        if player.balance == 0:
            print('\nЭто конечная.. Сейчас кого-то будут убивать.')
            status = False

def debt_offer(player):
    choice = deck_service.player_choice('\nЖелаешь взять долг? (y/n): ')
    if choice == 'y':
        deck_service.take_debt(player)

def pay_off_debt(player):
    print(f'\nБаланс: {player.balance} х.к.')
    print(f'Долг: {player.debt} х.к.')
    choice = deck_service.player_choice('\nЖелаешь выплатить долг долг? (y/n): ')
    if choice == 'y':
        deck_service.pay_off_debt(player)

def start_game(player, dealer, deck):
    print(f'\nБаланс: {player.balance} х.к.')
    print(f'Долг: {player.debt} х.к.')
    bet = deck_service.bet_validation(player)
    deck_service.show_2_cards(player, dealer, deck)
    if player_turn(player, dealer, deck, bet) != 'lose':
        dealer_turn(player, dealer, deck, bet)

def player_turn(player, dealer, deck, bet):
    print('\nХОД ИГРОКА')
    choice = deck_service.player_choice('\nТянуть следующую карту? (y/n): ')
    while choice == 'y':
        blackjack_view.print_player_draw_card()
        player.hand = deck_service.draw_cards(player.hand, 1, deck)
        player.update_value()
        blackjack_view.print_cards_player_turn(player, dealer)
        if player.value < 21:
            choice = deck_service.player_choice('\nТянуть следующую карту? (y/n): ')
        elif player.value > 21:
            player_lose(player, dealer, deck, bet)
            return 'lose'
        else:
            choice = 'n'

def dealer_turn(player, dealer, deck, bet):
    print('\nХОД КРУПЬЕ')
    blackjack_view.print_cards_dealer_turn(player, dealer)
    while dealer.value < 17:
        blackjack_view.print_dealer_draw_card()
        dealer.hand = deck_service.draw_cards(dealer.hand, 1, deck)
        dealer.update_value()
        blackjack_view.print_cards_dealer_turn(player, dealer)
    if dealer.value > 21:
        player_win(player, dealer, deck, bet)
    elif dealer.value > player.value:
        player_lose(player, dealer, deck, bet)
    elif dealer.value < player.value:
        player_win(player, dealer, deck, bet)
    else:
        draw(player, dealer, deck)

def player_lose(player, dealer, deck, bet):
    print('\nТы проиграл!')
    player.balance -= bet
    if player.debt:
        deck_service.charging_interest(player)
    deck_service.refresh_game(player, dealer, deck)
    time.sleep(0.5)

def player_win(player, dealer, deck, bet):
    print('\nТы выиграл!')
    player.balance += bet
    if player.debt:
        deck_service.charging_interest(player)
    deck_service.refresh_game(player, dealer, deck)
    time.sleep(0.5)

def draw(player, dealer, deck):
    print('\nНичья!')
    if player.debt:
        deck_service.charging_interest(player)
    deck_service.refresh_game(player, dealer, deck)
    time.sleep(0.5)


if __name__ == "__main__":
     main()