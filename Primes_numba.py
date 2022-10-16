from numba import jit

@jit()
def prime_py(range_start, range_end):
    """ ـ  حساب كم الأعداد الأولية الموجودة في مجال معين"""  
    count_of_primes = 0
    range_start = range_start if range_start >= 2 else 2
    for num in range(range_start, range_end + 1):
        for div_num in range(2, num):
            if ((num % div_num) == 0):
                break
        else:
            count_of_primes += 1
    return count_of_primes