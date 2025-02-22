import blackjack_view_st as view
import deck_service_st as service
import streamlit as st

def main():
    st.markdown("<h1 style='text-align: center; color: white;'>ПОХОЖДЕНИЯ НОВИЧКА</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: white;'>CHAPTER TWO: ОЧКО</h3>", unsafe_allow_html=True)
    if 'hello' not in st.session_state:
        view.hello(st)
        service.init(st)
    if st.session_state['button_start'] == True:
        service.button_start(st)
    else:
        player, dealer, deck = st.session_state['player'], st.session_state['dealer'], st.session_state['deck']
        if (player.balance > player.debt and player.debt > 0) and ('debt_pay_off_choice' not in st.session_state or st.session_state['debt_pay_off_choice'] == 'y'):
            pay_off_debt(player, st)
        elif player.balance == 0 and player.debt == 0:
            debt_offer(player, dealer, deck, st)
        elif player.balance >= 3000 and player.debt == 0:
            st.write(f'Баланс: {player.balance} х.к.')
            st.write(f'Долг: {player.debt} х.к.')
            st.write('Поздравляю, малой! Ты успешно справился со своей задачей! Увидимся в следующей части серии.')
            service.restart_game(player, dealer, deck, st)
        if player.balance == 0 or player.debt > 3000:
            st.write(f'Баланс: {player.balance} х.к.')
            st.write(f'Долг: {player.debt} х.к.')
            st.write('Это конечная.. Сейчас кого-то будут убивать.')
            service.restart_game(player, dealer, deck, st)
        start_game(player, dealer, deck, st)


def start_game(player, dealer, deck, st):
    while 'bet' not in st.session_state:
        st.session_state['bet'] = service.bet_validation(player, st)
        st.rerun()
    bet = st.session_state['bet']
    service.draw_2_cards(player, dealer, deck, st)
    while 'player_turn' not in st.session_state or st.session_state['player_turn'] == False:
        player_turn(player, dealer, deck, bet, st)
    dealer_turn(player, dealer, deck, bet, st)

def pay_off_debt(player, st):
    while 'debt_pay_off_choice' not in st.session_state:
        st.write(f'Баланс: {player.balance} х.к.')
        st.write(f'Долг: {player.debt} х.к.')
        st.session_state['debt_pay_off_choice'] = service.debt_player_choice(player, st, 'Желаешь выплатить долг?')
        st.rerun()       
    choice = st.session_state['debt_pay_off_choice']
    if choice == 'y':
        service.pay_off_debt(player, st)
    else:
        st.rerun()
        
def debt_offer(player, dealer, deck, st):
    st.write(f'Баланс: {player.balance} х.к.')
    st.write(f'Долг: {player.debt} х.к.')
    while 'debt_offer_choice' not in st.session_state:
        st.session_state['debt_offer_choice'] = service.debt_player_choice(player, st, 'Желаешь взять долг?')
        st.rerun()
    choice = st.session_state['debt_offer_choice']
    if choice == 'y':
        service.take_debt(player, st)
    else:
        st.write('Тогда начинай сначала лол')
        service.restart_game(player, dealer, deck, st)    
    

def player_turn(player, dealer, deck, bet, st):
    st.write('')
    st.write('ХОД ИГРОКА')
    while 'choice' not in st.session_state:
        st.session_state['choice'] = service.player_choice(player, dealer, st)
        st.rerun()
    choice = st.session_state['choice']
    while choice == 'y':
        player.draw_1_cards(deck)
        if player.value < 21:
            del st.session_state['choice']
            while 'choice' not in st.session_state:
                st.session_state['choice'] = service.player_choice(player, dealer, st)
                choice = st.session_state['choice']
                st.stop()
        elif player.value > 21:
            st.session_state['player_turn'] = False
            st.session_state['button_restart'] = True
            player_lose(player, dealer, deck, bet, st)
        else:
            choice = 'n'
    st.session_state['player_turn'] = True
    st.session_state['button_restart'] = True
    st.rerun()

def dealer_turn(player, dealer, deck, bet, st):
    st.write('')
    st.write('ХОД КРУПЬЕ')
    while dealer.value < 17:
        dealer.draw_1_cards(deck)
    if dealer.value > 21:
        player_win(player, dealer, deck, bet, st)
    elif dealer.value > player.value:
        player_lose(player, dealer, deck, bet, st)
    elif dealer.value < player.value:
        player_win(player, dealer, deck, bet, st)
    else:
        draw(player, dealer, deck, st)


def player_lose(player, dealer, deck, bet, st):
    if st.session_state['button_restart'] == True:
        if st.session_state['player_turn'] == False:
            view.print_cards_player_turn(player, dealer, st)
        else:
            view.print_cards_dealer_turn(player, dealer, st)
        st.write('Ты проиграл!')
        button = st.button('Продолжить')
    if not button:
        st.stop()
    else:
        player.balance -= bet
        if player.debt:
            service.charging_interest(player)
        service.refresh_game(player, dealer, deck, st)
        st.rerun()

def player_win(player, dealer, deck, bet, st):
    if st.session_state['button_restart'] == True:
        view.print_cards_dealer_turn(player, dealer, st)
        st.write('Ты выиграл!')
        button = st.button('Продолжить')
    if not button:
        st.stop()
    else:
        player.balance += bet
        if player.debt:
            service.charging_interest(player)
        service.refresh_game(player, dealer, deck, st)
        st.rerun()

def draw(player, dealer, deck, st):
    if st.session_state['button_restart'] == True:
        view.print_cards_dealer_turn(player, dealer, st)
        st.write('Hичья!')
        button = st.button('Продолжить')
    if not button:
        st.stop()
    else:
        if player.debt:
            service.charging_interest(player)
        service.refresh_game(player, dealer, deck, st)
        st.rerun()

if __name__ == "__main__":
     main()