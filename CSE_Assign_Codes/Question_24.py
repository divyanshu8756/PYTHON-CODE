import time
import sys


def order_mod(a, n):
    k = 1
    current_power = a % n
    while current_power != 1:
        k = k + 1
        current_power = (current_power * a) % n
        if k > n:
            return 0
    return k


def main_execution():
    print("Enter base a:")
    a = int(input())
    print("Enter modulus n:")
    n = int(input())

    start_time = time.perf_counter_ns()

    k = order_mod(a, n)

    end_time = time.perf_counter_ns()

    execution_time_ns = end_time - start_time

    memory_a = sys.getsizeof(a)
    memory_n = sys.getsizeof(n)
    memory_k = sys.getsizeof(k)
    total_memory_bytes = memory_a + memory_n + memory_k

    print("The smallest positive integer k such that a^k = 1 mod n is:")
    if k == 0:
        print("Order does not exist or exceeds the search limit n.")
    else:
        print(k)

    print("Memory utilisation (in bytes):", total_memory_bytes)
    print("Execution time (in nanoseconds):", execution_time_ns)


main_execution()
