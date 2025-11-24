import time
import sys


def aliquot_sum(n):
    s = 0
    if n <= 1:
        return 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s


def run_script():
    try:
        n_str = input("Enter a positive integer: ")
        n = int(n_str)
    except ValueError:
        print("Invalid input: Please enter a whole number.")
        return

    if n <= 0:
        print("Input must be a positive integer.")
        return

    start_time_ns = time.perf_counter_ns()

    result = aliquot_sum(n)

    end_time_ns = time.perf_counter_ns()

    execution_time_ns = end_time_ns - start_time_ns

    result_memory_bytes = sys.getsizeof(result)

    print("Sum of proper divisors:", result)
    print("Memory utilization:", result_memory_bytes, "bytes")
    print("Execution time:", execution_time_ns, "nanoseconds")


run_script()
