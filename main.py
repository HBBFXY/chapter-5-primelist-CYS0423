def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    if N <= 2:
        return ""  # 小于2的数没有质数
    
    # 初始化筛子：sieve[i]表示i是否为质数（初始假设都是质数）
    sieve = [True] * N
    sieve[0], sieve[1] = False, False  # 0和1不是质数
    
    # 筛选过程：从2开始，将其倍数标记为非质数
    for current in range(2, int(N ** 0.5) + 1):
        if sieve[current]:  # 如果current是质数，标记其倍数
            # 从current*current开始标记（更小的倍数已被之前的数标记过）
            sieve[current*current : N : current] = [False] * len(sieve[current*current : N : current])
    
    # 收集所有质数，转换为字符串后用空格连接
    primes = [str(i) for i, is_prime in enumerate(sieve) if is_prime]
    return ' '.join(primes)
