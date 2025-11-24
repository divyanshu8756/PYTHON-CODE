import time
import sys
import math


def is_square(n):
    if n < 0:
        return False
    root = int(math.isqrt(n))
    return root * root == n


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_fibonacci_prime(n):
    is_fibo = is_square(5 * n * n + 4) or is_square(5 * n * n - 4)
    return is_fibo and is_prime(n)


try:
    user_input = int(input("Enter an integer: "))
except:
    print("Invalid input.")
    sys.exit()

start_time_ns = time.perf_counter_ns()
result = is_fibonacci_prime(user_input)
end_time_ns = time.perf_counter_ns()

execution_time_ns = end_time_ns - start_time_ns
memory_bytes = sys.getsizeof(result)

print(f"Result: {result}")
print(f"Memory utilisation (in bytes): {memory_bytes}")
print(f"Execution time (in nanoseconds): {execution_time_ns}")
