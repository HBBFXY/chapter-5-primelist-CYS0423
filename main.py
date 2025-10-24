import math

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
    
    # 使用math.isqrt获取精确整数平方根（避免浮点误差）
    max_current = math.isqrt(N)
    for current in range(2, max_current + 1):
        if sieve[current]:  # 若current是质数，标记其所有倍数为非质数
            # 从current的平方开始标记（更小的倍数已被之前的质数标记）
            sieve[current*current : N : current] = [False] * len(sieve[current*current : N : current])
    
    # 收集所有质数（从2开始遍历，彻底杜绝1）
    primes = [str(i) for i in range(2, N) if sieve[i]]
    
    # 用空格连接，确保格式正确
    return ' '.join(primes)
