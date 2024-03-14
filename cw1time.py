import time

def suma_liczb_do(a):
    sum = 0
    for number in range(1, a+1):
        sum += number
    return sum

def suma_liczb_do2(a):
    return sum([number for number in range(1, a+1)])

def suma_liczb_do3(a):
    return sum({number for number in range(1, a+1)})

def suma_liczb_do4(a):
    return ((1+a)/2 * a)

def timer(start):
    end = time.perf_counter()
    return end-start


start = time.perf_counter()
print(suma_liczb_do(3000000))
print(timer(start))

start = time.perf_counter()
print(suma_liczb_do2(3000000))
print(timer(start))

start = time.perf_counter()
print(suma_liczb_do3(3000000))
print(timer(start))

start = time.perf_counter()
print(suma_liczb_do4(3000000))
print(timer(start))
