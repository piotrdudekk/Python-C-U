import time

def function_perf(func, *arg, how_many_times = 1):
    start = time.perf_counter()
    for i in range(0, how_many_times):
        func(*arg)
    end = time.perf_counter()
    return end - start

def is_in(container, number):
    if number in container:
        return True
    else:
        return False
 


setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

#print(is_in(listContainer, 99999))

print(function_perf(is_in, setContainer, 499, how_many_times = 2000))
print(function_perf(is_in, listContainer, 499, how_many_times = 2000))      
