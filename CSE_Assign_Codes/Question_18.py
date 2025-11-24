import time
import sys


def get_digit_product(n):
    p = 1
    for d in str(n):
        p *= int(d)
    return p


def multiplicative_persistence(n):
    c = 0
    while n >= 10:
        n = get_digit_product(n)
        c += 1
    return c


t_start = time.perf_counter_ns()

try:
    n_input_str = input("Enter a number: ")
    n = int(n_input_str)

    if n < 0:
        print("Please enter a non-negative number.")
        sys.exit()

    result = multiplicative_persistence(n)

except ValueError:
    print("Invalid input. Please enter a valid integer.")
    sys.exit()

t_end = time.perf_counter_ns()

time_ns = t_end - t_start

memory_bytes = sys.getsizeof(n) + sys.getsizeof(result)

print("Multiplicative Persistence:", result)
print("Memory Utilisation (bytes):", memory_bytes)
print("Execution Time (nanoseconds):", time_ns)
