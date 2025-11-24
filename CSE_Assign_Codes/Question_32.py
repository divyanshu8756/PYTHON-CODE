import random
import math
import time
import tracemalloc


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def pollard_rho(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    def f(x): return (x * x + c) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
        if d == n:
            return n
    return d


if __name__ == "__main__":
    try:
        n = int(input("Enter an integer to factor: "))

        tracemalloc.start()
        start_time = time.time_ns()

        factor = pollard_rho(n)

        end_time = time.time_ns()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"One factor is: {factor}")
        print(f"Memory Utilisation: {peak} bytes")
        print(f"Execution Time: {end_time - start_time} nanoseconds")

    except Exception as e:
        print(f"An error occurred: {e}")
