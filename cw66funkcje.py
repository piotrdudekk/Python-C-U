
def czy_parzyste(num):
    for i in num:
        if (i % 2 == 0):
            return True
    return False

def any_even(num):
    return any([x % 2 == 0 for x in num])

def all_even(num):
    return all([x % 2 == 0 for x in num])

numbers1 = [1, 3, 5, 6, 7]
numbers2 = [1, 3, 5, 7, 9]

numbers3 = [2, 4, 8, 10]

#print(czy_parzyste(numbers1))
#print(czy_parzyste(numbers2))

#print(any_even(numbers1))
#print(any_even(numbers2))

print(all_even(numbers1))
print(all_even(numbers2))
print(all_even(numbers3))
