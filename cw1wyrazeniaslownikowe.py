'''
liczby = [1,2,3,4,5,6,7,8]

multiplied = {number : number*(number+1)
              for number in liczby
              }

print(multiplied)

#imiona ze zbioru zaczynające się na A i ich długość

names = {"Arkadiusz", "Piotr", "Antoni", "Nikola", "Amanda", "Amadeusz", "Miłosz"}

namesLength = {
    name : len(name)
    for name in names
    if (name.startswith("A"))
    }

print(namesLength)
'''

#celsjusze na farenheity

celcius = {"t1" : -20, "t2" : -14, "t3" : 0, "t4" : 12, "t5" : 24}
'''
fahrenheit = {
        temp : (celcius[temp] * 1.8 + 32)
        for temp in celcius
    }
'''

fahrenheit = {
        key : celcius * 1.8 +32
        for key, celcius in celcius.items()
    }
print(fahrenheit)
