import pyximport; pyximport.install()
from Primes_cython import prime_py
print(prime_py(0,100000))