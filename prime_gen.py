def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True        
num=2
primes = []
get_stop = True
while get_stop:
    stop = input('What number should the script stop at? (-1 is a bad idea)\n')
    try:
        stop = int(stop)
        get_stop = False
    except ValueError:
        print('Not an integer')
find = True
while find:
    ip = is_prime(num)
    if ip:
        primes.append(num)
        print(num)
    if num == stop:
        find = False
    num += 1
