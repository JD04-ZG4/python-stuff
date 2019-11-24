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
start = get_int('What number should the script start at?\n')
stop = get_int('What number should the script stop at? (entering a number before the start point is a bad idea)\n')
print()
num=start
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
