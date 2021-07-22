import timeit
import random

def using_max(array):
    best = -float('inf')
    for val in array:
        best = max(best, val)
    return best

def using_comp(array):
    best = -float('inf')
    for val in array:
        if best < val: best = val
    return best


arr1 = [random.randint(-1000, 1000) for _ in range(100000)]

res1 = using_max(arr1)
res2 = using_comp(arr1)

#res1 = timeit.timeit("using_max(arr1)", number=1000, setup="from __main__ import using_max, arr1")
#res2 = timeit.timeit("using_comp(arr1)", number=1000, setup="from __main__ import using_comp, arr1")

print(res1)
print(res2)