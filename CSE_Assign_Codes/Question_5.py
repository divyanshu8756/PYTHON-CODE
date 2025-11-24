import time
import tracemalloc


def is_abundant(n):
    divisors_sum = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum > n


try:
    user_input = int(input("Enter a number: "))

    tracemalloc.start()
    start_time = time.time_ns()

    result = is_abundant(user_input)

    end_time = time.time_ns()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(result)
    print(f"Memory Utilisation: {peak} bytes")
    print(f"Execution Time: {end_time - start_time} nanoseconds")

except ValueError:
    print("Please enter a valid integer.")
