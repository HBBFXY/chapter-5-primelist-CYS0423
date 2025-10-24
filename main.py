# -*- coding: utf-8 -*-
def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    # 处理N小于等于2的情况（无质数）
    if N <= 2:
        return ""
    
    # 初始化筛法列表，sieve[i]表示i是否为质数
    sieve = [True] * N
    sieve[0], sieve[1] = False, False  # 0和1不是质数
    
    # 筛选过程：标记非质数
    for current in range(2, int(N ** 0.5) + 1):
        if sieve[current]:  # 若current是质数，标记其倍数为非质数
            # 从current的平方开始标记（更小的倍数已被处理）
            sieve[current*current : N : current] = [False] * len(sieve[current*current : N : current])
    
    # 收集所有质数并转换为字符串
    primes = [str(i) for i, is_prime in enumerate(sieve) if is_prime]
    return ' '.join(primes)
