from collections import Counter
from functools import cmp_to_key

# f = open('input_test.txt')
f = open('input.txt')


def card_type(card):
    c = Counter(card)
    v = sorted(list(c.values()), reverse=True)
    if 5 in v:
        return 6
    if 4 in v:
        return 5
    if 3 in v and 2 in v:
        return 4
    if 3 in v:
        return 3
    if v[0] == 2 and v[1] == 2:
        return 2
    if v[0] == 2:
        return 1
    return 0


scores = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def scored_card(card):
    return [scores[c] for c in card]


def compare(item1, item2):
    (card1, _) = item1
    (card2, _) = item2
    type_1 = card_type(card1)
    type_2 = card_type(card2)
    if type_1 > type_2:
        return 1
    if type_2 > type_1:
        return -1

    scored1 = scored_card(card1)
    scored2 = scored_card(card2)
    for c1, c2 in zip(scored1, scored2):
        if c1 > c2:
            return 1
        if c2 > c1:
            return -1
    return 0


deck = []
for line in f.readlines():
    l = line.strip()
    if not l:
        continue
    card, bid = l.split()
    deck.append((card, int(bid)))

deck.sort(key=cmp_to_key(compare))
s = 0
for rank, (card, bid) in enumerate(deck):
    s += bid * (rank+1)
print(s)
