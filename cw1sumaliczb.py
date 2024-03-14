
def suma_liczb_do(a):
    sum = 0
    for number in range(1, a+1):
        sum += number
    return sum

def suma_liczb_do2(a):
    return sum([number for number in range(1, a+1)])

def suma_liczb_do3(a):
    return sum({number for number in range(1, a+1)})

def suma_liczb_do4(a):
    return ((1+a)/2 * a)


liczba = int(input("Podaj liczbę: "))
print(suma_liczb_do3(liczba))
