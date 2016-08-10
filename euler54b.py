#Comparing hands that are the same (getting high card, kicker etc.)

def high_card(hand):
    return cv(sort_hand(hand)[-1])


def straight(hand):
    hand = sort_hand(hand)
    if cv(hand[0]) == 2 and cv(hand[1]) == 3 and cv(hand[2]) == 4 and cv(hand[3]) == 5 and cv(hand[4]) == 14:
        return 5
    else:
        return hand[-1][0]
