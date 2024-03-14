
imiona = ["Arkadiusz", "Wiola", "Antek"]

imie = input("Podaj twoje imię: ")
imie = imie.capitalize()

if (imie in imiona):
    print("Masz dostęp.")
else:
    print("Nie masz dostępu.")
