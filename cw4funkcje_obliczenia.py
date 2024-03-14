import figury
from enum import IntEnum

Menu_Figur = IntEnum("Menu_Figur", "Koło, Kwadrat, Prostokąt, Trójkąt, Trapez")

wybor = int(input("""Czego pole chcesz obliczyć?
1 - koła,
2 - kwadratu,
3 - prostokąta,
4 - trójkąta,
5 - trapezu:
"""))

if (wybor == Menu_Figur.Koło):
    r = float(input("Podaj promień: "))
    print(figury.pole_kola(r))

elif (wybor == Menu_Figur.Kwadrat):
    a = float(input("Podaj bok kwadratu: "))
    print(figury.pole_kwadratu(a))

elif (wybor == Menu_Figur.Prostokąt):
    a = float(input("Poadj pierwszy bok: "))
    b = int(input("Poadj drugi bok: "))
    print(figury.pole_prostokata(a, b))

elif (wybor == Menu_Figur.Trójkąt):
    a = float(input("Poadj podstawę: "))
    h = float(input("Poadj wysokość: "))
    print(figury.pole_trojkata(a, h))

elif (wybor == Menu_Figur.Trapez):
    a = float(input("Poadj pierwszą podstawę: "))
    b = float(input("Poadj drugą podstawę: "))
    h = float(input("Poadj wysokość: "))
    print(figury.pole_trapezu(a, b, h))

else:
    print("Podana zła wartość.")
