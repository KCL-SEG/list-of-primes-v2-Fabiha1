"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

from contextlib import nullcontext


def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError("Argument must be greater than 0")
    else:
        count = 2
        is_prime = True
        while len(list) < number_of_primes:
            for i in range(2,count):
                if count % i == 0:
                    is_prime = False
                    break

            if is_prime:
                list.append(count)
            
            is_prime = True
            count+=1
            
    return list

print(primes(20))
