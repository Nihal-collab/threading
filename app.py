import threading
import time
import multiprocessing
from datetime import datetime

start_time = time.time() 
print(datetime.now())

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def sum_of_prime(i):
    total = 0
    for j in range(2, i+1):
        if is_prime(j):
            total += j
    print(f"Sum of primes till {i} = {total}")

l = [10000, 20000, 30000, 40000, 50000]

threads = []
# for i in l:
#     t = threading.Thread(target=sum_of_prime, args=(i,))
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()

if __name__ == '__main__':
    for i in l:
        t = multiprocessing.Process(target=sum_of_prime, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

end_time = time.time() 
elapsed_time = end_time - start_time 

print(datetime.now())
print(f"{elapsed_time:.3f} seconds") 
