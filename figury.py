import math

def pole_kwadratu(a):
    return a * a

def pole_prostokata(a, b):
    return a * b

def pole_kola(r):
    return math.pi * r ** 2

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_trapezu(a, b, h):
    return (a + b) / 2 * h
'''  
figura = input("Pole jakiej figury chcesz policzyć? Podaj: kwadrat/prostokąt/koło/trójkąt/trapez: ")
figura = figura.lower()

if (figura == "kwadrat"):
    bok = int(input("Podaj długość boku: "))
    print(pole_kwadratu(bok))

elif (figura == "prostokąt" or figura == "prostokat"):
    bok1 = int(input("Podaj długość pierwszego boku: "))
    bok2 = int(input("Podaj długość drugiego boku: "))
    print(pole_prostokata(bok1, bok2))

elif (figura == "koło" or figura == "kolo"):
    promien = int(input("Podaj długość promienia: "))
    print(pole_kola(promien))

elif (figura == "trójkąt" or figura == "trojkat"):
    podst = int(input("Podaj długość podstawy: "))
    wys = int(input("Podaj wysokość: "))
    print(pole_trojkata(podst, wys))

elif (figura == "trapez"):
    podst1= int(input("Podaj długość pierwszej podstawy: "))
    podst2= int(input("Podaj długość drugiej podstawy: "))
    wys = int(input("Podaj wysokość: "))
    print(pole_trapezu(podst1, podst2, wys))

else:
    print("Została podana zła wartość")
'''
