def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    if N <= 2:
        return ""  # 小于2的数没有质数
    
    # 初始化筛法列表：sieve[i]表示i是否为质数
    sieve = [True] * N
    sieve[0], sieve[1] = False, False  # 明确排除0和1
    
    # 筛选非质数：从2开始，标记其倍数为非质数
    for current in range(2, int(N ** 0.5) + 1):
        if sieve[current]:  # 若current是质数，标记其倍数
            # 从current的平方开始标记（更小的倍数已被处理）
            sieve[current*current : N : current] = [False] * len(sieve[current*current : N : current])
    
    # 收集质数，严格排除1（即使筛法出错也双重保障）
    primes = []
    for i in range(2, N):  # 直接从2开始遍历，彻底避免1
        if sieve[i]:
            primes.append(str(i))
    
    # 用空格连接，确保格式正确（无首尾空格、无连续空格）
    return ' '.join(primes)
