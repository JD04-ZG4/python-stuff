def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True        
num=2
primes = []
while True:
    ip = is_prime(num)
    if ip:
        primes.append(num)
        print(num)
    num += 1
