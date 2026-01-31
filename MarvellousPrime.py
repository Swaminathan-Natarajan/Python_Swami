def ChkPrime(Arr):
    prime = []
    for num in Arr:
        if num > 1:  # primes are greater than 1
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime.append(num)
    return prime
 
