def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True
def get_int(text):
    while True:
        usr_input = input(text)
        try:
            usr_input = int(usr_input)
            return usr_input
        except ValueError:
            print('Not an integer')
stop = get_int('What number should the script stop at? (-1 is a bad idea)\n')
num=2
primes = []
find = True
while find:
    ip = is_prime(num)
    if ip:
        primes.append(num)
        print(num)
    if num == stop:
        find = False
    num += 1
