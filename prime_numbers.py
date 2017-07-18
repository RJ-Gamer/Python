import math# v1
import time
def prime_v1(n):
    """ Return True if 'n' is prime, False otherwise"""
    if n == 1:
        return False
    for d in range(2, n):
        if n%d == 0:
            return False
    return True
"""
#=============== TEST FUNCTION ===========#
for n in range(1, 20):
    print(n, prime_v1(n))
"""
"""
#=========== Time Test ===============
t0 = time.time()
for n in range(1, 1000):
    prime_v1(n)
t1 = time.time()
print("Time Required:", t0 - t0)
"""
def prime_v2(n):
    if n == 1:
        return False
    max_divisor = int(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

def prime_v3(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_divisor = int(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

#=========== Time Test ===============
t0 = time.time()
for n in range(1, 1000000):
    prime_v3(n)
t1 = time.time()
print("Time Required by v2:", t1 - t0)
