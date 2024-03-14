#krotki w słowniku

'''
listaPracownikow = {
                    ("Piotr", 22, "Nowy Sącz", 2),
                    ("Miłosz", 23, "Kielce", 2),
                    ("Karol", 23, "Kielce", 10),
                    ("Tomasz", 49, "Zgierz", 13)
                    }

for imie, wiek, miasto, staz in listaPracownikow:
    print ("Imię:", imie)
    print ("Wiek:", wiek)
    print ("Miasto:", miasto)
    print ("Staż w miesiącach:", staz)
    print()


#słowniki w liście

ratings2 = [
        {'name': "Arkadiusz", 'ratings': (2,1,2,3,2,3), 'behaviour': 4},
        {'name': "Agness", 'ratings': (4,2,1,3,4), 'behaviour': 2}
    ]
for dictionary in ratings2:
    for key in dictionary:
        print (key, ":", dictionary[key])
    print()
'''

#słownik w słowniku
'''
    #sposób 1

people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},          
         }

for key in people:
    print("ID:", key)
    for key2 in people[key]:
        print(key2, ":", people[key][key2])
    print()

'''


    #sposób 2

people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},          
         }

#print(people.items()) - tworzy listę z krotkami po 2 wartości - zwykłą i słownik
'''
(people = [
           ('IcFDG2bO9AYDF651DoyH', {'name': 'John', 'age': 27, 'sex': 'Male'}),
           ('KcD9ntE6IRM59vkVta1k', {'name': 'Marie', 'age': 22, 'sex': 'Female'}...),
'''

for id, dictionary in people.items():
    print("ID:", id)
    for key in dictionary:
        print(key, ":", dictionary[key])
    print()

              
