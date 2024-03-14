
names = {"Arkadiusz", "bartłomiej", "kasia", "Basia", "Aleksandra", "olga"}

names2 = {
        name.capitalize()
        for name in names
        if not name.startswith("B")
    }

print(names2)
