
def get_primes(n):
    primes = []
    for possiblePrime in range(2, n + 1):
        # 假设该数是素数
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                # 如果该数可以被除1和自身外的其他数整除，那么它不是素数
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes


# 测试函数
print(*get_primes(100))
