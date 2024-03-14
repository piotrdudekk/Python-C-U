wynik = 0

i = 0

while (i<3):
    x = int(input("Podaj dodatnią liczbę parzystą: "))
    if (x%2 == 0 and x>0):
        wynik += x
    else:
        print("Liczba miała być DODATNIA I PARZYSTA!")
        continue
    i += 1

print("Wynik dodawania 3 dodatnich liczb parzystych to:", wynik)
