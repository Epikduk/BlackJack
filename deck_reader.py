deck_path = 'resources/deck.txt'
card_value_path = 'resources/card_value.txt'

def read_deck():
    deck = {}
    with open(deck_path, 'r', encoding='utf-8') as file1, open(card_value_path, 'r', encoding='utf-8') as file2:
        for line in file1:
            deck[line.strip()] = int(file2.readline().strip())
    return deck
