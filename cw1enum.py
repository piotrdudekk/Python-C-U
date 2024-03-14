from enum import IntEnum

#kolory = ['czerwony', 'niebieski', 'czarny', 'fioletowy']
kolory = {'czerwony':1, 'niebieski':2, 'czarny':3, 'fioletowy':4}

Menu_Kolor = IntEnum("Menu_Kolor", kolory)

wybor_kolor = int(input("Wybierz kolor: 1.czerwony, 2.niebieski, 3.czarny, 4.fioletowy: "))


if (wybor_kolor == Menu_Kolor.czerwony):
    print("Twój ulubiony kolor to CZERWONY!")

elif (wybor_kolor == Menu_Kolor.niebieski):
    print("Twój ulubiony kolor to NIEBIESKI!")

elif (wybor_kolor == Menu_Kolor.czarny):
    print("Twój ulubiony kolor to CZARNY!")

elif (wybor_kolor == Menu_Kolor.fioletowy):
    print("Twój ulubiony kolor to FIOLETOWY!")
