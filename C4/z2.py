def is_prime(*nums: int):
    for n in nums:
        prime = True if n > 1 else False
        for i in range(2, int(n/2)+1):
            if not prime: break
            if n % i == 0: prime = False
        print(f"{n} is ", " a prime" if prime else " not a prime")


is_prime(0, 1, 2, 3, 4, 5)
