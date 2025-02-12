import repository
import time

def main():
    hello()
    repository.init()
    player = Player()
    dealer = Dealer()
    status = True
    while status:
        start_game(player, dealer)
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

def hello():
     print('\nНу привет новеньй (старенький?). Ты показал неплохие результаты в умении рассказывать анекдоты.')
     print('Однако тебя ждет следующее испытание: сыграть в очко с паханом.')
     print('На старте твой банк составляет 1000 хлебных крошек (х.к.). Твоя цель заключается в наборе 3000 х.к.')
     print('Знай, если сильно проиграешься, то ты можешь залезть в долги. Тебе будет предложено взять до 2000 дополнительных х.к.')
     print('Долг платежом красен, а потому у тебя будут накапливаться проценты по задолженности (15 %) после каждой сыгранной партии.')
     print('Проценты будут начисляться до тех пор, пока долг не будешь погашен. Ты не сможешь одержать победу, пока не выплатишь свой долг.')
     print('При достижении величины долга свыше 3000 х.к., ты проиграешь')

class Hand():
    def __init__(self):
        self.hand = {}
        self.value = 0

    def draw_2_cards(self):
        self.hand = repository.draw_cards(self.hand, 2)
        self.update_value()

    def draw_1_cards(self):
        self.hand = repository.draw_cards(self.hand, 1)
        self.update_value()

    def update_value(self):
        self.value = 0
        for card in self.hand:
            self.value += self.hand[card]
        if self.value > 21:
            self.check_aces()

    def check_aces(self):
        for card in self.hand:
            if self.hand[card] == 11 and self.value > 21:
                self.hand[card] = 1
                self.value -= 10

    def print_cards(self):
        time.sleep(0.5)
        print(', '.join(self.hand.keys()) + f'. (Сумма очков: {self.value})')

class Dealer(Hand):
    def __init__(self):
        super().__init__()
    
    def print_start_cards(self):
        time.sleep(0.5)
        first_card = list(self.hand)[0]
        print(f'{first_card}, ***' + f'. (Сумма очков: ***)')

class Player(Hand):
    def __init__(self):
        super().__init__()
        self.balance = 1000
        self.debt = 0


def debt_offer(player):
    choice = repository.player_choice('\nЖелаешь взять долг? (y/n): ')
    if choice == 'y':
        repository.take_debt(player)

def pay_off_debt(player):
    print(f'\nБаланс: {player.balance} х.к.')
    print(f'Долг: {player.debt} х.к.')
    choice = repository.player_choice('\nЖелаешь выплатить долг долг? (y/n): ')
    if choice == 'y':
        repository.pay_off_debt(player)

def start_game(player, dealer):
    print(f'\nБаланс: {player.balance} х.к.')
    print(f'Долг: {player.debt} х.к.')
    bet = repository.bet_validation(player)
    repository.show_2_cards(player, dealer)
    if player_turn(player, dealer, bet) != 'lose':
        dealer_turn(player, dealer, bet)

def player_turn(player, dealer, bet):
    print('\nХОД ИГРОКА')
    choice = repository.player_choice('\nТянуть следующую карту? (y/n): ')
    while choice == 'y':
        repository.print_player_draw_card()
        player.draw_1_cards()
        repository.print_cards_player_turn(player, dealer)
        if player.value < 21:
            choice = repository.player_choice('\nТянуть следующую карту? (y/n): ')
        elif player.value > 21:
            player_lose(player, dealer, bet)
            return 'lose'
        else:
            choice = 'n'

def dealer_turn(player, dealer, bet):
    print('\nХОД КРУПЬЕ')
    repository.print_cards_dealer_turn(player, dealer)
    while dealer.value < 17:
        repository.print_dealer_draw_card()
        dealer.draw_1_cards()
        repository.print_cards_dealer_turn(player, dealer)
    if dealer.value > 21:
        player_win(player, dealer, bet)
    elif dealer.value > player.value:
        player_lose(player, dealer, bet)
    elif dealer.value < player.value:
        player_win(player, dealer, bet)
    else:
        draw(player, dealer)

def player_lose(player, dealer, bet):
    print('\nТы проиграл!')
    player.balance -= bet
    if player.debt:
        repository.charging_interest(player)
    repository.refresh_game(player, dealer)
    time.sleep(0.5)

def player_win(player, dealer, bet):
    print('\nТы выиграл!')
    player.balance += bet
    if player.debt:
        repository.charging_interest(player)
    repository.refresh_game(player, dealer)
    time.sleep(0.5)

def draw(player, dealer):
    print('\nНичья!')
    if player.debt:
        repository.charging_interest(player)
    repository.refresh_game(player, dealer)
    time.sleep(0.5)


if __name__ == "__main__":
     main()