from collections import Counter

ranks = {11:"J",12:"Q",13:"K",14:"A"}

nums = {"J":11,"Q":12,"K":13,"A":14}

def rank_to_num(rank):
    return nums.get(rank,int(rank))

def num_to_rank(num):
    if num <= 10:
        return str(num)
    else:
        return ranks.get(num)

def tie_breaker(cards, num):


    return []


def flush(cards):

    return []


def straight(cards):
    return []

def hand(hole_cards, community_cards):

    cards = hole_cards + community_cards

    kind = tie_breaker(cards, 5)

    flush_lst = flush(cards)

    straight_lst = straight(cards)
    

    return "nothing", ["2","3",'4','5','6']

if __name__ == "__main__":
    hand(["2♠", "3♦"], ["2♣", "2♥", "3♠", "3♥", "2♦"])
    print("Le Fin")
