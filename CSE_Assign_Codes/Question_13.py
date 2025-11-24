import time
import sys
import os


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


def is_mersenne_prime(p):
    if not is_prime(p):
        return False
    m = (1 << p) - 1
    s = 4
    for i in range(3, p + 1):
        s = (s * s - 2) % m
    return s == 0


p = int(input("Enter a number: "))

start_time = time.perf_counter_ns()
result = is_mersenne_prime(p)
end_time = time.perf_counter_ns()

execution_time_ns = end_time - start_time
memory_usage_bytes = sys.getsizeof(p) + sys.getsizeof(result)

print(f"2^{p} - 1 is {'a Mersenne prime' if result else 'not a Mersenne prime'}")
print(f"Execution time: {execution_time_ns} nanoseconds")
print(f"Memory utilization: {memory_usage_bytes} bytes")
