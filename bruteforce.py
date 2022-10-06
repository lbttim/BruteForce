import itertools
from multiprocessing import Pool
from concurrent.futures.process import ProcessPoolExecutor
import string
import time

def guess_password(real):
    start = time.time()
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits 
    attempts = 0
    for password_length in range(1,15):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            print(str(guess)+", "+str(attempts))
            if guess != real:
               pass
            else:
                end = time.time()
                print(end - start)
                return 'password is {}. found in {} guesses.'.format(guess, attempts)

print(guess_password('1234'))