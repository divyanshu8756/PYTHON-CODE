import time
import tracemalloc


def get_proper_divisors_sum(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total


def is_deficient(n):
    divisors_sum = get_proper_divisors_sum(n)
    return divisors_sum < n


if __name__ == "__main__":
    num = int(input("Enter a number: "))

    tracemalloc.start()
    start_time = time.time_ns()

    result = is_deficient(num)

    end_time = time.time_ns()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Is deficient: {result}")
    print(f"Execution time: {end_time - start_time} nanoseconds")
    print(f"Memory utilisation: {peak} bytes")
