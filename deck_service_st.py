import blackjack_view_st as view
import entities_st

def init(st):
    st.session_state['deck'] = entities_st.Deck()
    st.session_state['player'] = entities_st.Player()
    st.session_state['dealer'] = entities_st.Dealer()
    st.session_state['deck'].refresh_current_deck()
    st.session_state['hello'] = True
    st.session_state['button_start'] = True

def button_start(st):
    button_start = st.button('Приступить к игре', type = 'primary', icon = ':material/accessible_forward:')
    if not button_start:
        st.stop()
    else:
        st.session_state['button_start'] = False
        st.rerun()

def bet_validation(player, st):
    st.write(f'Баланс: {player.balance} х.к.')
    st.write(f'Долг: {player.debt} х.к.')
    bet = st.text_input('Введи сумму ставки')
    if bet == '':
        st.stop()
    try:
        bet = int(bet)
        if bet > player.balance:
            st.write('Ставка превышает размер баланса!')
            st.stop()
        elif bet <= 0:
            st.write('Размер ставки должен быть положительным числом!')
            st.stop()
    except ValueError:
        st.write('Должно быть введено число!')
        st.stop()
    return bet

def draw_cards(hand, cards, deck):
    for i in range(cards):
        card = deck.current_deck.pop()
        card_cost = deck.return_card_cost(card)
        hand[card] = card_cost
    return hand

def draw_2_cards(player, dealer, deck, st):
    if len(player.hand) == 0 and len(dealer.hand) == 0:
        player.draw_2_cards(deck)
        dealer.draw_2_cards(deck)

def print_x_cards(x, cards, st):
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    columns = [col1, col2, col3, col4, col5, col6, col7, col8]
    i = 0
    for col in columns:
        if i < x:
            with col:
               st.image(f'resources/{cards[i]}.png')
               i += 1
        else:
            continue

def print_dealer_cards(self, cards, st):
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    with col1:
        st.image(f'resources/{cards[0]}.png')
    with col2:
        st.image(f'resources/question_mark.png')

def player_choice(player, dealer, st):
    view.print_cards_player_turn(player, dealer, st)
    st.write('Тянуть следующую карту?')
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    yes, no = False, False
    with col1:
        yes = st.button('Да')
    with col2:
        no = st.button('Нет')
    if not yes and not no:
        st.stop()
    elif yes:
        choice = 'y'
    elif no:
        choice = 'n'
    return choice

def debt_player_choice(player, st, str):
    st.write(str)
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    yes, no = False, False
    with col1:
        yes = st.button('Да')
    with col2:
        no = st.button('Нет')
    if not yes and not no:
        st.stop()
    elif yes:
        choice = 'y'
    elif no:
        choice = 'n'
    return choice

def pay_off_debt(player, st):
    player.balance -= player.debt
    player.debt = 0
    del st.session_state['debt_pay_off_choice']
    
def take_debt(player, st):
    player.debt = player_take_debt(st)
    player.balance += player.debt
    del st.session_state['debt_offer_choice']
    st.rerun()

def player_take_debt(st):
    debt = st.text_input('Введи сумму займа (до 2000 х.к.)')
    if debt == '':
        st.stop()
    try:
        debt = int(debt)
        if debt > 2000:
            st.write('Сумма займа не должна превышать 2000 х.к.!')
            st.stop()
        elif debt <= 0:
            st.write('Сумма займа должна быть положительным числом!')
            st.stop()
    except ValueError:
        st.write('Должно быть введено число!')
        st.stop()
    return debt


def charging_interest(player):
    player.debt *= 1.15
    player.debt = round(player.debt)

def refresh_game(player, dealer, deck, st):
    deck.refresh_current_deck()
    player.hand = {}
    dealer.hand = {}
    player.value = 0
    dealer.value = 0
    st.session_state['button_restart'] = False
    if 'bet' in st.session_state:
        del st.session_state['bet']
    if 'choice' in st.session_state:
        del st.session_state['choice']
    if 'debt_offer_choice' in st.session_state:
        del st.session_state['debt_offer_choice']
    if 'debt_pay_off_choice' in st.session_state:
        del st.session_state['debt_pay_off_choice']
    if 'player_turn' in st.session_state:
        del st.session_state['player_turn']

def restart_game(player, dealer, deck, st):
    button_restart = st.button('Начать сначала', type = 'primary')
    if not button_restart:
        st.stop()
    else:
        refresh_game(player, dealer, deck, st)
        player.balance = 1000
        player.debt = 0
        st.rerun()