import time
import math
import sys


def count_distinct_prime_factors(n):
    if n < 2:
        return 0
    count = 0
    if n % 2 == 0:
        count += 1
        while n % 2 == 0:
            n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
    if n > 1:
        count += 1
    return count


n = int(input("Enter a number: "))

start_time = time.perf_counter_ns()
result = count_distinct_prime_factors(n)
end_time = time.perf_counter_ns()

execution_time_ns = end_time - start_time

vars_size = sys.getsizeof(n) + sys.getsizeof(result) + \
    sys.getsizeof(execution_time_ns)

print(result)
print(f"Memory utilized: {vars_size} bytes")
print(f"Execution time: {execution_time_ns} nanoseconds")
