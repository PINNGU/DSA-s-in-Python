#radix sort , similar to counting as it uses part of its algorithm but we focus on the least significant digit and move up in digits
#we sort by digits , using buckets to store each value by its digit (we have as many buckets as the base)
#time complexity is weird but in good cases (when maximum number isnt in billions , like in counting sort, and most cases are base 10) it has decent complexity - O(d*(n+k))

from plotting import plot_array
import matplotlib.pyplot as plt

def radix(numbers):

    m = max(numbers)
    digit = 0
    while m > 0:
        m = m // 10
        digit = digit + 1

    d = 0

    while d < digit:

        buckets = [[],[],[],[],[],[],[],[],[],[]]

        for n in numbers:
            lsd = n // (10 ^ d)
            lsd = lsd % 10
            buckets[lsd].append(n)
            
        
        numbers.clear()
        

        for k in buckets:
            numbers.extend(k)

        d = d + 1

   

    print(numbers)

