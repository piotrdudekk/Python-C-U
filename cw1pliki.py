'''
try:
    file = open("test", "w") #uchwyt

    file.write("uzhdfiuedsrdb")
    print(0/0)

finally:
    file.close()
'''

with open("oceany.txt", "w") as file:
    file.write('''Atlantycki
Sokojny
Południowy
Arktyczny
Indyjski''')

    
    
