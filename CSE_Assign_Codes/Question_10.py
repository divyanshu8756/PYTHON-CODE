import time
import tracemalloc


def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
    if n > 2:
        factors.append(n)
    return factors


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))

        tracemalloc.start()
        start_time = time.time_ns()

        result = prime_factors(num)

        end_time = time.time_ns()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"Prime factors: {result}")
        print(f"Memory utilisation: {peak} bytes")
        print(f"Execution time: {end_time - start_time} nanoseconds")

    except ValueError:
        print("Please enter a valid integer.")
