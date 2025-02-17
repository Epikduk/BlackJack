def read_deck():
    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['крести', 'буби', 'черви', 'пики']
    deck = []
    for suit in suits:
        for value in card_values:
            card = f'{value} {suit}'
            deck.append(card)
    return deck

def read_costs(deck):
    costs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card_costs = {}
    index = 0
    for suits in range(4):
        for cost in range(len(costs)):
            card_costs[deck[index]] = costs[cost]
            index += 1
    return card_costs
