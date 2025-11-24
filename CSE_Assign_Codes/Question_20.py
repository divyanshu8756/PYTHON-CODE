import time
import sys


def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result


def run_calculation():
    print("Enter base:")
    base = int(input())
    print("Enter exponent:")
    exponent = int(input())
    print("Enter modulus:")
    modulus = int(input())

    start_time_ns = time.perf_counter_ns()
    final_result = mod_exp(base, exponent, modulus)
    end_time_ns = time.perf_counter_ns()

    execution_time_ns = end_time_ns - start_time_ns
    memory_usage_bytes = sys.getsizeof(final_result)

    print("Calculated Value (base^exponent % modulus):", final_result)
    print("Memory Utilisation (bytes):", memory_usage_bytes)
    print("Execution Time (nanoseconds):", execution_time_ns)


run_calculation()
