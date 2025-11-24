import math
import time
import tracemalloc


def is_perfect_power(n):
    if n == 1:
        return True
    if n < 1:
        return False
    limit = int(math.log2(n))
    for b in range(2, limit + 1):
        a = round(n ** (1 / b))
        if a ** b == n:
            return True
    return False


tracemalloc.start()

try:
    user_input = int(input("Enter a number: "))

    start_time = time.time_ns()
    result = is_perfect_power(user_input)
    end_time = time.time_ns()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Is perfect power: {result}")
    print(f"Memory Utilisation: {peak} bytes")
    print(f"Execution Time: {end_time - start_time} nanoseconds")

except ValueError:
    print("Please enter a valid integer.")
    tracemalloc.stop()
