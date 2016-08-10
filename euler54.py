hands = []
with open ('p054_poker.txt') as inputfile:
    for i in inputfile:
        hands.append(i[:-1].split(' '))
splithands= []
for hand in hands:
    splithands.append([hand[:5],hand[5:]])
deals = splithands

def cv(card):
    if card[0].isdigit():
        return int(card[0])
    if card[0] == 'T':
        return 10
    elif card[0] == 'J':
        return 11
    elif card[0] == 'Q':
        return 12
    elif card[0] == 'K':
        return 13
    elif card[0] == 'A':
        return 14

def sort_hand(hand):
    return sorted(hand, key=cv)

def is_flush(hand):
    suit = hand[0][-1]
    for card in hand:
        if card[-1] != suit:
            return False
    return True

def is_straight(hand):
    hand = sort_hand(hand)
    for i in range (1,len(hand)):
        if cv(hand[i]) != cv(hand[i-1]) + 1:
            return False
    return True

def get_combos(hand):
    combos = {}
    for card in hand:
        if card[0] not in combos:
            combos[card[0]] = 1
        else:
            combos[card[0]] += 1
    return combos

def is_4ok(hand):
    combos = get_combos(hand)
    for value in combos:
        if combos[value] == 4:
            return True
    return False

def is_full_house(hand):
    if len(get_combos(hand)) == 2 and not is_4ok(hand):
        return True

def is_3ok(hand):
    combos = get_combos(hand)
    for value in combos:
        if combos[value] == 3:
            return True
    return False

def get_straight_high(hand):
    return sort_hand(hand)[-1][0]

for hands in deals:
    for hand in hands:
        if is_straight(hand):
            print get_straight_high(hand)
            print hand
            raw_input()
