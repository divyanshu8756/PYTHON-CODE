import time
import sys


def count_divisors(k):
    count = 0
    i = 1
    while i * i <= k:
        if k % i == 0:
            if i * i == k:
                count = count + 1
            else:
                count = count + 2
        i = i + 1
    return count


def is_highly_composite(n):
    if n <= 0:
        return False
    if n == 1:
        return True

    n_divisors = count_divisors(n)

    for k in range(1, n):
        k_divisors = count_divisors(k)
        if k_divisors >= n_divisors:
            return False

    return True


def run_analysis():
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
    except ValueError:
        print("Invalid input")
        return

    start_time_ns = time.perf_counter_ns()

    result = is_highly_composite(number)

    end_time_ns = time.perf_counter_ns()

    execution_time_ns = end_time_ns - start_time_ns

    memory_input = sys.getsizeof(number)
    memory_output = sys.getsizeof(result)

    print("Is the number highly composite:", result)
    print("Memory utilization:", memory_input + memory_output, "bytes")
    print("Execution time:", execution_time_ns, "nanoseconds")


run_analysis()
