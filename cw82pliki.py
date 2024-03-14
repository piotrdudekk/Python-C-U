
osoby = []

with open("imionanazwiska.txt", "r", encoding = "UTF-8") as imionanazwiska:
    for line in imionanazwiska:
        osoby.append(tuple(line.replace("\n", "").split(" ")))


print(osoby)
