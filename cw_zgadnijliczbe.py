liczba = 23

i=0

while (i<1):
    x = int(input("Zgadnij liczbę: "))
    if (x == liczba):
        print("Gratulacje, zgadłeś! Szukana liczba to ", liczba, ".")
        break
    elif (x < 0):
        print("Niestety nie, szukamy liczby dodatniej. Spróbuj ponownie.")
        continue
    elif (x > 0 and x < liczba):
        print("Niestety nie, szukana liczba jest większa od podanej. Spróbuj ponownie.")
        continue
    else:
        print("Niestety nie, szukana liczba jest mniejsza od podanej. Spróbuj ponownie.")
        continue

    x += 1

    
        
