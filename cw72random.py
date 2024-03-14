import random


def random_numbers1(rang, amount):
    x = 0
    win_numbers = []
    while x < amount:
        a = random.randint(1, rang)
        if a not in win_numbers:
            win_numbers.append(a)
            x += 1
    return win_numbers

def random_numbers2(rang, amount):
    return random.sample(range(1, rang+1), amount)


print(random_numbers1(49, 6))
print(random_numbers2(49, 6))


