def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    primes = []
    # 遍历从2到N-1的所有数（质数必须大于1）
    for num in range(2, N):
        # 2是唯一的偶数质数，单独处理
        if num == 2:
            primes.append(str(num))
            continue
        # 排除所有偶数（除2外，偶数不可能是质数）
        if num % 2 == 0:
            continue
        # 检查奇数是否为质数：只需验证到sqrt(num)
        is_prime = True
        sqrt_num = int(num **0.5) + 1  # +1确保覆盖平方根整数部分
        # 只检查奇数除数（步长为2）
        for i in range(3, sqrt_num, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    # 用空格连接所有质数字符串，空列表会返回空字符串
    return ' '.join(primes)
