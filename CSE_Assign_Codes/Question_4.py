import sys
import time
import tracemalloc


def digital_root(n):
    while n >= 10:
        sum_digits = 0
        temp_n = n
        while temp_n > 0:
            sum_digits += temp_n % 10
            temp_n //= 10
        n = sum_digits
    return n


def main():
    try:
        n = int(input("Enter a number: "))

        tracemalloc.start()
        start_time = time.time_ns()

        result = digital_root(n)

        end_time = time.time_ns()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        execution_time = end_time - start_time

        print(f"Digital Root: {result}")
        print(f"Memory Utilisation: {peak} bytes")
        print(f"Execution Time: {execution_time} nanoseconds")

    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
