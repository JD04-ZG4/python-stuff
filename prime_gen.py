# Creates a function that checks if a number is prime
def is_prime(num):
    if num < 2:
        return False # All numbers under 2 aren't primes, so they are skipped
    for i in range(2,num): # Goes through every number from 2 to the number being checked
        if num%i == 0: # If a number is divisible by a number between 2 and it it isn't prime
            return False
    return True # If both tests are passed then it must be prime

# Converts text to int and loops until a valid input is given
def get_int(text):
    while True: # Loops until user enters valid input
        usr_input = input(text) # Gets user input using the passed text
        try:
            usr_input = int(usr_input) # Converts usr_input to int
            return usr_input # If the input was valid, the value is returned
        except ValueError:
            print('Not an integer') # If the integer conversion failed, The user is notified and it loops
try:
    num = get_int('What number should the script start at?\n') #Gets the integer to start at
    stop = get_int('What number should the script stop at? (entering a number before the start point is a bad idea)\n') #Gets the integer to finish at
except: # Assigns default values when being tested
    num = 2
    stop = 1000
print() # Prints a new line to make reading the output more clear
primes = [] # Creates an empty list to store primes in
find = True # Creates the variable for the script to loop
while find: # Loops until the target is reached
    ip = is_prime(num) # Sees if the number is prime
    if ip:
        primes.append(num) # If the number is prime, it is added to the list
        print(num) # The number is printed
    if num == stop:
        find = False # Stops if the target is reached
    num += 1 # Increases the value of num
