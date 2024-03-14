def dodaj_definicje(key, definition, definitions):
    definitions[key] = definition
    print("Definicja dodana poprawnie")
    return

def znajdz_definicje(key, definitions):
    if key in definitions:
        return definitions[key]
    else:
        return "Nie znaleziono definicji o nazwie", key

def usun_definicje(key, definitions):
    if key in definitions:
        del definitions[klucz]
        print("Usunięto definicję o nazwie:", klucz)
    else:
        print("Nie znaleziono definicji o nazwie", klucz)
    return



definicje = {}
 
while(True):
    print("1: Dodaj definicję")
    print("2: Znajdź definicję")
    print("3: Usuń definicję")
    print("4: Zakończ")
 
    wybor = input("Co chcesz zrobić? ")
 
    if (wybor == "1"):
        klucz = input("Podaj klucz (słowo) do zdefiniowania: ")
        definicja = input("Podaj definicję: ")
        dodaj_definicje(klucz, definicja, definicje)
    
    elif (wybor == "2"):
        klucz = input("Czego szukasz? ")
        print (znajdz_definicje(klucz, definicje))
        
    elif (wybor == "3"):
        klucz = input("Jaką definicję chcesz usunąć? ")
        usun_definicje(klucz, definicje)
        
    elif (wybor == "4"):
        print("No to pa!")
        break
    else:
        print("Podałeś coś z poza zakresu")
