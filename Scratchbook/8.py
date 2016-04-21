#! /bin/us/python3.5
from sympy.ntheory.factor_ import primefactors
from datashape.discovery import isnull
from numba.cgutils import is_null
from networkx.classes.function import is_empty


#===============================================================================
# The first two consecutive numbers to have two distinct prime factors are:
# 
# 14 = 2 × 7
# 15 = 3 × 5
# 
# The first three consecutive numbers to have three distinct prime factors are:
# 
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# 
# Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
#===============================================================================

def main():
    
    i = 0
    numbers = list()
    collection = list()

    while len(numbers)!=4:
        i +=1 
        x = prime_factors(i)
        if len(x) > 4:
            if len(collection)==0: 
                collection.append(x)
                numbers.append(i)
            elif numbers[-1]+1==i and x  not in collection: 
                collection.append(x)
                numbers.append(i)
            else:
                del numbers[:]
                del collection[:]
    print("{} : {}".format(numbers, collection))

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors     

 
if __name__ == "__main__": main()
