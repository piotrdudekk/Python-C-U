import random


print('''Gra polega na przejściu 5 ruchów przez jaskinię. Podczas każdego ruchu gracz
ma szansę (60%) trafić na skrzynię. Skrzynie mają różne kolory, oznaczające
prawdopodobieństwo ich wystąpienia. Zielona, w której gracz znajdzie około 1000
złota, trafia się z prawdopodobieństwem 75%, pomarańczowa (ok. 4000 złota) 20%,
fioletowa(ok. 9000 złota) 4%, a legendarna złota skrzynia (ok. 16000 złota) - 1%.
Dokładne ilości złota znajdujące się w skrzyniach miogą być max. 10% mniejsze
i 10% większe od podanych wartości. ''')
print()

def approximateValue(value):
    lowestValue = value - value * 0.1
    highestValue = value + value * 0.1
    return random.randint(lowestValue, highestValue)

def next_move(first_rand, second_rand, in_chest):
    cash = 0
    first = random.choices(first_rand, [0.6, 0.4])
    if (first == ["chest"]):
        print("Gratulacje! Trafiłeś na skrzynię.")
        second = random.choices(second_rand, [0.75, 0.2, 0.04, 0.01])
        if (second == ["green"]):
            apr_cash = approximateValue(in_chest[0])
            print("Znalazłeś skrzynię zieloną. Wygrywasz", apr_cash, "złota!")
            cash += apr_cash
        elif (second == ["orange"]):
            apr_cash = approximateValue(in_chest[1])
            print("Znalazłeś skrzynię pomarańczową. Wygrywasz", apr_cash, "złota!")
            cash += apr_cash
        elif (second == ["purple"]):
            apr_cash = approximateValue(in_chest[2])
            print("Znalazłeś skrzynię fioletową. Wygrywasz", apr_cash, "złota!")
            cash += apr_cash
        elif (second == ["gold"]):
            apr_cash = approximateValue(in_chest[3])
            print("UWAGA! Znalazłeś legendarną złotą skrzynię! Wygrywasz", apr_cash, "złota!")
            cash += apr_cash
    elif (first == ["nothing"]):
        print("Niestety, nie trafiłeś żadnej skrzyni.")
    return cash


    
choice = ["chest", "nothing"]
chests = ["green", "orange", "purple", "gold"]
moneyInChest = [1000, 4000, 9000, 16000]
money = 0

#start gry
name = input("Podaj swoje imię aby rozpocząć grę: ")
print("Witaj", name, "!")
move = input("Naciśnij enter aby wykonać pierwszy ruch.")
print()
money = money + next_move(choice, chests, moneyInChest)


for i in range (9999999999):
    print()
    move = input("Naciśnij enter aby wykonać kolejny ruch.")
    print()
    money = money + next_move(choice, chests, moneyInChest)
    
print()
print("Jestem z Ciebie dumny,", name, ". Udało Ci się ukończyć grę! Masz na koncie", money, "złota!")
end = input("Naciśnij dowolny przycisk, aby zakończyć grę.")
