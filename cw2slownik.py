print ("0 - koniec programu, 1 - dodaj osobę, 2 - usuń osobę, 3 - znajdź osobę")

people = {}

x=4

while (x != '0'):
    x = input("Co chcesz zrobić? Wybierz liczbę od 0 do 3: ")

    if (x != '1' and x!= '2' and x != '3' and x != '0'):
        print ("Zła wartość. Podaj wartość ponownie.")

    elif (int(x) == 1):
        name = input("Podaj imię: ")
        name = name.capitalize()
        surname = input("Podaj nazwisko: ")
        surname = surname.capitalize()
        age = int(input("Podaj wiek: "))
        id=0
        for key in people:
            id += 1
        people[id+1] = {"imię": name, "nazwisko": surname, "wiek": age}

    elif (int(x) == 2):
        print("Oto lista osób:")
        print(people)
        while (1):
            nr = int(input("Podaj numer osoby, którą chcesz usunąć z listy:"))

            a=0
            for id in people:
                if (id == nr): a += 1
            if (a == 1):
                del people[nr]
                break
            else:
                print("Podanej osoby nie ma na liście.")
                y = int(input("Aby zakończyć proces usuwania 0, aby kontynuować - 1: "))
                if (y == 0):
                    break

    elif (int(x) == 3):
        while (1):
            name = input("Podaj imię: ")
            name = name.capitalize()
            surname = input("Podaj nazwisko: ")
            surname = surname.capitalize()
            b=0
            for id in people:
                for key in people[id]:
                    if (people[id][key] == name and people[id]["nazwisko"] == surname):
                        b=1
                        c = people[id]
            if (b == 1):
                print(c)
                break
            else:
                print("Nie ma na liście osoby o takim imieniu i nazwisku.")
                y = int(input("Aby zakończyć wyszukiwanie wybierz 0, aby kontynuować - 1: "))
                if (y == 0):
                    break

        
    
        
