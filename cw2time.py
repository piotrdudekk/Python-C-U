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

def function_perf(func, arg, how_may_times=1):
    start = time.perf_counter()
    for i in range(0, how_may_times):
        func(arg)
    end = time.perf_counter()
    return end-start


print(function_perf(suma_liczb_do, 5000000, 4))

print(function_perf(suma_liczb_do2, 5000000, 4))

print(function_perf(suma_liczb_do3, 5000000, 4))

print(function_perf(suma_liczb_do4, 5000000, 4))
