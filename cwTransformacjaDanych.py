#liczby od 100 do 470 podzielne przez 7, ale nie przez 5

#wyrażenie listowne

numbers1 = [number
            for number in range(100, 471)
            if number % 7 == 0
            if number % 5 != 0
    ]

print(numbers1)

#generator

numbers2 = (
        number
        for number in range(100, 471)
        if number % 7 == 0
        if number % 5 != 0
    )

for number in numbers2:
    print(number)

#wyrażenie zbioru

numbers3 = {
        number
        for number in range(100, 471)
        if number % 7 == 0
        if number % 5 != 0
    }

print(numbers3)

#wyrażenie słownikowe

numbers4 = {
        number : (number/7, number%5)
        for number in range(100, 471)
        if number % 7 == 0
        if number % 5 != 0
    }

print(numbers4)
