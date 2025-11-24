import time
import sys


def sum_proper_divisors(n):
    total = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != 1 and i * i != n:
                total += n // i
    return total


def are_amicable(a, b):
    if a <= 1 or b <= 1:
        return False
    sum_a = sum_proper_divisors(a)
    sum_b = sum_proper_divisors(b)
    return sum_a == b and sum_b == a


def main():
    try:
        n1_str = input("Enter the first number: ")
        n2_str = input("Enter the second number: ")

        n1 = int(n1_str)
        n2 = int(n2_str)
    except ValueError:
        print("Invalid input. Please enter whole numbers.")
        return

    start_time = time.perf_counter_ns()

    result = are_amicable(n1, n2)

    end_time = time.perf_counter_ns()
    execution_time_ns = end_time - start_time

    memory_usage = sys.getsizeof(n1_str) + sys.getsizeof(n2_str) + \
        sys.getsizeof(n1) + sys.getsizeof(n2) + sys.getsizeof(result)

    print(
        f"Result: {'The numbers are amicable.' if result else 'The numbers are NOT amicable.'}")
    print(f"Memory Utilisation (bytes): {memory_usage}")
    print(f"Execution Time (nanoseconds): {execution_time_ns}")


if __name__ == "__main__":
    main()
