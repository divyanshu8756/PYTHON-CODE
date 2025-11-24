import random
import time
import tracemalloc


def is_prime_miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


if __name__ == "__main__":
    try:
        n_input = int(input("Enter number to test (n): "))
        k_input = int(input("Enter number of rounds (k): "))
        tracemalloc.start()
        start_time = time.time_ns()
        result = is_prime_miller_rabin(n_input, k_input)
        end_time = time.time_ns()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Is Prime: {result}")
        print(f"Execution Time: {end_time - start_time} nanoseconds")
        print(f"Memory Utilisation: {peak} bytes")
    except ValueError:
        print("Invalid input")
