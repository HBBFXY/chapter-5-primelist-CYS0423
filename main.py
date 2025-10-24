# 在此文件中实现 PrimeList 函数

def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    def is_prime(m):
    if m <= 1:
        return False
    if m == 2:
        return True
    if m % 2 == 0:
        return False
    for i in range(3, int(m**0.5) + 1, 2):
        if m % i == 0:
            return False
    return True

def PrimeList(N):
    primes = []
    for num in range(2, N):
        if is_prime(num):
            primes.append(str(num))
    return ' '.join(primes)
