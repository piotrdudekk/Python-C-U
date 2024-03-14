import random

def cards_dealer(cards, players):
    random.shuffle(cardList)
    playersList = {}
    
    for i in range (1, players+1):
        playersList[i] = []


    if (len(cards) % players == 0):
        while len(cards) > 0:
            for i in range(1, players+1):
                playersList[i].append(cards[-1])
                cards.pop(-1)
    else:
        while len(cards) >= players:
            for i in range(1, players+1):
                playersList[i].append(cards[-1])
                cards.pop(-1)

    return playersList


print("Aplikacja rozdaje karty od dziewiątek do Jokerów podanej ilości graczy.")


cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]

while 1:
    number_of_players = int(input("Podaj liczbę graczy (2-6): "))
    if (1<number_of_players<7):
        break
    else:
        print("Zła ilość. Podaj ilość graczy ponownie.")

print(cards_dealer(cardList, number_of_players))

