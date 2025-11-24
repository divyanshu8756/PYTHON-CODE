import time
import math
import tracemalloc


def is_composite(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False


def is_carmichael(n):
    if not is_composite(n):
        return False
    for a in range(2, n):
        if math.gcd(a, n) == 1:
            if pow(a, n - 1, n) != 1:
                return False
    return True


if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))

        tracemalloc.start()
        start_time = time.time_ns()

        result = is_carmichael(n)

        end_time = time.time_ns()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"Is Carmichael number: {result}")
        print(f"Memory utilisation: {peak} bytes")
        print(f"Execution time: {end_time - start_time} nanoseconds")

    except ValueError:
        print("Invalid input")
