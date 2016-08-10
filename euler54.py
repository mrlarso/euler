hands = []
with open ('p054_poker.txt') as inputfile:
    for i in inputfile:
        hands.append(i[:-1].split(' '))
splithands= []
for hand in hands:
    splithands.append([hand[:5],hand[5:]])
deals = splithands

#get card value
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
    return False

def is_flush(hand):
    suit = hand[0][-1]
    for card in hand:
        if card[-1] != suit:
            return False
    return True

def is_straight(hand):
    hand = sort_hand(hand)
    if cv(hand[0]) == 2 and cv(hand[1]) == 3 and cv(hand[2]) == 4 and cv(hand[3]) == 5 and cv(hand[4]) == 14:
        return True
    for i in range (1,len(hand)):
        if cv(hand[i]) != cv(hand[i-1]) + 1:
            return False
    return True

def is_3ok(hand):
    combos = get_combos(hand)
    for value in combos:
        if combos[value] == 3:
            return True
    return False

def is_two_pair(hand):
    if len(get_combos(hand)) == 3 and not is_3ok(hand):
        return True
    return False


def is_pair(hand):
    if len(get_combos(hand)) == 4:
        return True
    return False

def is_high_card(hand):
    if len(get_combos(hand)) == 5:
        return True
    return False

def get_hand_value(hand):
    if is_straight(hand) and is_flush(hand) and sort_hand(hand)[-2][0] == "K":
        return 10
    if is_straight(hand) and is_flush(hand):
        return 9
    if is_4ok(hand):
        return 8
    if is_full_house(hand):
        return 7
    if is_flush(hand):
        return 6
    if is_straight(hand):
        return 5
    if is_3ok(hand):
        return 4
    if is_two_pair(hand):
        return 3
    if is_pair(hand):
        return 2
    return 1


for hands in deals:
    for hand in hands:
        print sort_hand(hand)
        print str(get_hand_value(hand))
        raw_input()
