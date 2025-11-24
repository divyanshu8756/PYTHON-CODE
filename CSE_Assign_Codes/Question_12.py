import time
import math
import sys
import os


def is_prime_power(n):
    if n <= 1:
        return False
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            return n == 1
    return True


n = int(input("Enter a number: "))

process = os.getpid()
py = __import__('psutil')
memory_before = py.Process(process).memory_info().rss

start_time = time.perf_counter_ns()

result = is_prime_power(n)

end_time = time.perf_counter_ns()
memory_after = py.Process(process).memory_info().rss

execution_time_ns = end_time - start_time
memory_used = memory_after - memory_before

print(f"{n} is prime power: {result}")
print(f"Memory utilized: {memory_used} bytes")
print(f"Execution time: {execution_time_ns} nanoseconds")
