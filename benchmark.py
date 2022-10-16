import timeit

Cython_Code = timeit.repeat(''' 
prime_py(0, 100000)
''',
'import pyximport; pyximport.install(); from Primes_cython import prime_py'
, repeat=3, number=1)
print("Cython best time:" , min(Cython_Code) ,"Seconds ✔ OP:",455189150/min(Cython_Code))


Numba_Code = timeit.repeat(''' 
prime_py(0, 100000)
''',
'from Primes_numba import prime_py'
, repeat=3, number=1)
print("Numba best time:" , min(Numba_Code) ,"Seconds ✔ OP:",455189150/min(Numba_Code))

Numba_Prange_Code = timeit.repeat(''' 
prime_py(0, 100000)
''',
'from Primes_numba_parallel import prime_py'
, repeat=3, number=1)
print("Numba Prange best time:" , min(Numba_Prange_Code) ,"Seconds ✔ OP:",455189150/min(Numba_Prange_Code))

Python_Vanilla_Code = timeit.repeat(''' 
prime_py(0, 100000)
''',
'from Primes_python import prime_py'
, repeat=3, number=1)
print("Python best time:" , min(Python_Vanilla_Code) ,"Seconds ✔ OP:",455189150/min(Python_Vanilla_Code))

