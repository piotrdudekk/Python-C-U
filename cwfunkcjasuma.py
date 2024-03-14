
def suma_dodatnich(numbers):
    suma = 0

    for number in numbers:
        if (number > 0):
            suma += number

    return suma

liczby = [-2, 8, 837837, -23, 0, 333]

print(suma_dodatnich(liczby))
